"""JS8Call LXMF Bot implementation for message forwarding between JS8Call and LXMF networks."""

import configparser
import json
import logging
import threading
import time
from collections import defaultdict
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler
from socket import AF_INET, SOCK_STREAM, socket

from lxmfy import IconAppearance, LXMFBot, pack_icon_appearance_field

from .storage.sqlite_storage import SQLiteStorage


class JS8CallBot:
    """JS8Call LXMF Bot for message forwarding between JS8Call and LXMF networks."""

    def __init__(self, name=None):
        """Initialize JS8Call LXMF Bot.

        Args:
            name: Bot name identifier (if None, will be read from config)

        """
        self.js8call_socket = None
        self.js8call_connected = False
        self.bot_location = None
        self.node_operator = None
        self.blocked_words = []

        self.cfg = configparser.ConfigParser()
        self.cfg.read("config.ini")

        if name is None:
            name = self.cfg.get("bot", "name", fallback="JS8Call-Bot")

        self.bot = LXMFBot(
            name=name,
            announce=self.cfg.getint("bot", "announce_interval", fallback=360),
            announce_immediately=True,
            admins=set(self.cfg.get("bot", "allowed_users", fallback="")
                      .strip().split(",")),
            hot_reloading=True,
            rate_limit=5,
            cooldown=10,
            max_warnings=3,
            warning_timeout=300,
            command_prefix="/",
            permissions_enabled=True,
            first_message_enabled=True,
            signature_verification_enabled=self.cfg.getboolean("bot", "signature_verification_enabled", fallback=False),
            require_message_signatures=self.cfg.getboolean("bot", "require_message_signatures", fallback=False),
        )

        icon_data = IconAppearance(
            icon_name="radio", fg_color=b"\xff\x45\x00", bg_color=b"\x00\x00\x80",
        )
        self.icon_lxmf_field = pack_icon_appearance_field(icon_data)

        self.db = SQLiteStorage(
            self.cfg.get("js8call", "db_file", fallback="js8call.db"),
        )
        if self.cfg.get("bot", "store_users_in_db", fallback="no").lower() in ("yes", "true", "1"):
            self.bot.storage = self.db

        self.setup_logging()
        self.setup_js8call()
        self.setup_state()

    def setup_logging(self):
        """Configure logging handlers and formatters."""
        self.logger = logging.getLogger("js8call_lxmf_bot")
        self.logger.setLevel(logging.INFO)

        handlers = [
            RotatingFileHandler(
                "js8call_lxmf_bot.log", maxBytes=1000000, backupCount=5,
            ),
            logging.StreamHandler(),
        ]

        for handler in handlers:
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def setup_js8call(self):
        """Initialize JS8Call connection settings."""
        self.js8call_server = (
            self.cfg.get("js8call", "host", fallback="localhost"),
            self.cfg.getint("js8call", "port", fallback=2442),
        )
        self.js8call_socket = None
        self.js8call_connected = False

        self.js8groups = self.cfg.get("js8call", "js8groups", fallback="").split(",")
        self.js8urgent = self.cfg.get("js8call", "js8urgent", fallback="").split(",")
        self.js8groups = [group.strip() for group in self.js8groups]
        self.js8urgent = [group.strip() for group in self.js8urgent]

    def setup_state(self):
        """Initialize bot state and load users from storage."""
        self.distro_list = set()
        self.user_groups = defaultdict(set)
        self.muted_users = defaultdict(set)
        self.start_time = time.time()
        self.load_state_from_storage()

    def load_state_from_storage(self):
        """Load users and their settings from storage."""
        try:
            users_data = self.bot.storage.get("users", {})
            if users_data:
                for user_hash, user_data in users_data.items():
                    self.distro_list.add(user_hash)
                    self.user_groups[user_hash] = set(user_data.get("groups", []))
                    self.muted_users[user_hash] = set(user_data.get("muted_groups", []))
            self.logger.info("Loaded %d users from storage", len(self.distro_list))
        except Exception as e:
            self.logger.error("Error loading state from storage: %s", e)

    def save_state_to_storage(self):
        """Save current state to storage."""
        try:
            users_data = {}
            for user in self.distro_list:
                users_data[user] = {
                    "groups": list(self.user_groups[user]),
                    "muted_groups": list(self.muted_users[user]),
                }
            self.bot.storage.set("users", users_data)
            self.logger.debug("Saved state to storage")
        except Exception as e:
            self.logger.error("Error saving state to storage: %s", e)

    def add_to_distro_list(self, user):
        """Add a user to the distribution list."""
        if user not in self.distro_list:
            self.distro_list.add(user)
            default_groups = self.cfg.get(
                "bot", "default_groups", fallback="",
            ).split(",")
            default_groups = [g.strip() for g in default_groups if g.strip()]
            for group in default_groups:
                self.user_groups[user].add(group)

            self.save_state_to_storage()

            welcome_msg = "You have been added to the JS8Call message group"
            if default_groups:
                welcome_msg += (
                    f" and the following default groups: {', '.join(default_groups)}"
                )
            welcome_msg += ". You will receive messages when they are available."
            self.bot.send(user, welcome_msg, lxmf_fields=self.icon_lxmf_field)

            self.logger.info("Added %s to distribution list", user)
        else:
            self.bot.send(user, "You are already in the JS8Call message group.", lxmf_fields=self.icon_lxmf_field)

    def remove_from_distro_list(self, user):
        """Remove a user from the distribution list."""
        if user in self.distro_list:
            self.distro_list.remove(user)
            self.user_groups.pop(user, None)
            self.muted_users.pop(user, None)

            self.save_state_to_storage()

            self.bot.send(
                user,
                "You have been removed from the JS8Call message group and all groups.",
                lxmf_fields=self.icon_lxmf_field,
            )
            self.logger.info("Removed %s from distribution list", user)
        else:
            self.bot.send(user, "You are not in the JS8Call message group.", lxmf_fields=self.icon_lxmf_field)

    def add_user_to_groups(self, user, groups):
        """Add a user to specified groups."""
        if user in self.distro_list:
            for group in groups:
                if group in self.js8groups or group in self.js8urgent:
                    self.user_groups[user].add(group)

            self.save_state_to_storage()

            self.bot.send(
                user,
                f"You have been added to the following groups: {', '.join(groups)}",
                lxmf_fields=self.icon_lxmf_field,
            )
            self.logger.info("Added %s to groups: %s", user, ", ".join(groups))
        else:
            self.bot.send(
                user,
                "You need to join the JS8Call message group first. Use /add command.",
                lxmf_fields=self.icon_lxmf_field,
            )

    def remove_user_from_group(self, user, group):
        """Remove a user from a specific group."""
        if user in self.distro_list and group in self.user_groups[user]:
            self.user_groups[user].remove(group)

            self.save_state_to_storage()

            self.bot.send(user, f"You have been removed from the group: {group}", lxmf_fields=self.icon_lxmf_field)
            self.logger.info("Removed %s from group: %s", user, group)
        else:
            self.bot.send(user, f"You are not in the group: {group}", lxmf_fields=self.icon_lxmf_field)

    def mute_user_groups(self, user, groups):
        """Mute a user from specified groups."""
        if user in self.distro_list:
            if "ALL" in [g.upper() for g in groups]:
                all_groups = set(self.js8groups + self.js8urgent)
                self.muted_users[user].update(all_groups)
                self.bot.send(user, "You have muted all available groups.", lxmf_fields=self.icon_lxmf_field)
                self.logger.info("Muted all groups for %s", user)
            else:
                muted = []
                for group in groups:
                    if group in self.js8groups or group in self.js8urgent:
                        self.muted_users[user].add(group)
                        muted.append(group)
                if muted:
                    self.bot.send(user, f"You have muted the following groups: {', '.join(muted)}", lxmf_fields=self.icon_lxmf_field)
                    self.logger.info("Muted %s for %s", ", ".join(muted), user)
                else:
                    self.bot.send(user, "No valid groups to mute.", lxmf_fields=self.icon_lxmf_field)
            self.save_state_to_storage()
        else:
            self.bot.send(user, "You need to join the JS8Call message group first. Use /add command.", lxmf_fields=self.icon_lxmf_field)

    def unmute_user_groups(self, user, groups):
        """Unmute a user from specified groups."""
        if user in self.distro_list:
            if "ALL" in [g.upper() for g in groups]:
                self.muted_users[user].clear()
                self.bot.send(user, "You have unmuted all groups.", lxmf_fields=self.icon_lxmf_field)
                self.logger.info("Unmuted all groups for %s", user)
            else:
                unmuted = []
                for group in groups:
                    if group in self.muted_users[user]:
                        self.muted_users[user].remove(group)
                        unmuted.append(group)
                if unmuted:
                    self.bot.send(user, f"You have unmuted the following groups: {', '.join(unmuted)}", lxmf_fields=self.icon_lxmf_field)
                    self.logger.info("Unmuted %s for %s", ", ".join(unmuted), user)
                else:
                    self.bot.send(user, "No valid groups to unmute or they were not muted.", lxmf_fields=self.icon_lxmf_field)
            self.save_state_to_storage()
        else:
            self.bot.send(user, "You need to join the JS8Call message group first. Use /add command.", lxmf_fields=self.icon_lxmf_field)

    def register_commands(self):
        """Register bot command handlers."""

        @self.bot.command(description="Add yourself to the JS8Call message group", admin_only=True)
        def add(ctx):
            self.add_to_distro_list(ctx.sender)

        @self.bot.command(description="Remove yourself from the JS8Call message group", admin_only=True)
        def remove(ctx):
            self.remove_from_distro_list(ctx.sender)

        @self.bot.command(description="Show available groups and your subscriptions")
        def groups(ctx):
            groups_output = self.show_groups(ctx.sender)
            ctx.reply(groups_output)

        @self.bot.command(description="Join one or more groups")
        def join(ctx):
            if ctx.args:
                self.add_user_to_groups(ctx.sender, ctx.args)
            else:
                ctx.reply("Usage: /join <group1> <group2> ...")

        @self.bot.command(description="Leave a specific group")
        def leave(ctx):
            if ctx.args:
                self.remove_user_from_group(ctx.sender, ctx.args[0])
            else:
                ctx.reply("Usage: /leave <group>")

        @self.bot.command(description="Mute one or more groups or ALL", threaded=True)
        def mute(ctx):
            if ctx.args:
                self.mute_user_groups(ctx.sender, ctx.args)
            else:
                ctx.reply("Usage: /mute <group1> <group2> ... or ALL")

        @self.bot.command(description="Unmute one or more groups or ALL", threaded=True)
        def unmute(ctx):
            if ctx.args:
                self.unmute_user_groups(ctx.sender, ctx.args)
            else:
                ctx.reply("Usage: /unmute <group1> <group2> ... or ALL")

        @self.bot.command(description="Show message log", threaded=True)
        def showlog(ctx):
            try:
                num_messages = int(ctx.args[0]) if ctx.args else 10
                log_output = self.show_log(num_messages)
                ctx.reply(log_output)
            except (IndexError, ValueError):
                ctx.reply("Usage: /showlog <number>")

        @self.bot.command(description="Show bot statistics", threaded=True)
        def stats(ctx):
            period = (
                ctx.args[0] if ctx.args and ctx.args[0] in ["day", "month"] else None
            )
            stats_output = self.show_stats(period)
            ctx.reply(stats_output)

        @self.bot.command(description="Show bot information")
        def info(ctx):
            info_output = self.show_info()
            ctx.reply(info_output)

        @self.bot.command(description="Show usage statistics", threaded=True)
        def analytics(ctx):
            period = (
                ctx.args[0] if ctx.args and ctx.args[0] in ["day", "week"] else None
            )
            analytics_output = self.show_analytics(period)
            ctx.reply(analytics_output)

    def run(self, *args, **kwargs):
        """Run the bot main loop."""
        self.logger.info("JS8Call LXMF Bot starting up...")
        self.register_commands()

        js8call_thread = threading.Thread(target=self.js8call_loop)
        js8call_thread.daemon = True
        js8call_thread.start()

        try:
            self.bot.run()
        except KeyboardInterrupt:
            self.logger.info("Shutting down JS8Call LXMF bot...")
        finally:
            if self.js8call_socket:
                try:
                    self.js8call_socket.close()
                except Exception:
                    self.logger.warning("Error closing JS8Call socket during cleanup")
            try:
                if hasattr(self.bot.storage, "cleanup"):
                    self.bot.storage.cleanup()
            except Exception as e:
                self.logger.warning("Error cleaning up storage: %s", e)
            try:
                if hasattr(self.db, "cleanup"):
                    self.db.cleanup()
            except Exception as e:
                self.logger.warning("Error cleaning up SQLite storage: %s", e)

    def js8call_loop(self):
        """Thread loop for maintaining JS8Call connection and processing messages.
        """
        while True:
            if not self.js8call_connected:
                self.connect_js8call()
            elif self.js8call_connected:
                self.process_js8call_messages()
            time.sleep(1)

    def connect_js8call(self):
        """Connect to JS8Call instance."""
        self.logger.info("Connecting to JS8Call on %s", self.js8call_server)
        self.js8call_socket = socket(AF_INET, SOCK_STREAM)
        try:
            self.js8call_socket.connect(self.js8call_server)
            self.js8call_connected = True
            self.logger.info("Connected to JS8Call")
        except Exception as e:
            self.logger.error("Failed to connect to JS8Call: %s", e)
            self.js8call_socket = None
            self.js8call_connected = False

    def process_js8call_messages(self):
        """Process messages from JS8Call."""
        if not self.js8call_connected:
            return

        try:
            data = self.js8call_socket.recv(4096).decode("utf-8")
            if not data:
                self.js8call_connected = False
                self.logger.warning("JS8Call connection lost")
                return

            messages = data.strip().split("\n")
            for message in messages:
                try:
                    if not message:
                        continue
                    msg_data = json.loads(message)
                    self.handle_js8call_message(msg_data)
                except json.JSONDecodeError as e:
                    self.logger.error("Failed to parse JS8Call message: %s", e)
                    continue

        except Exception as e:
            self.logger.error("Error processing JS8Call messages: %s", e)
            self.js8call_connected = False

    def handle_js8call_message(self, data):
        """Handle a single JS8Call message."""
        try:
            if data["type"] == "RX.DIRECTED":
                parts = data["value"].split(":")
                if len(parts) < 2:
                    self.logger.warning(
                        "Invalid directed message format: %s", data["value"],
                    )
                    return

                sender = parts[0].strip()
                content = ":".join(parts[1:]).strip()

                if any(word.lower() in content.lower() for word in self.blocked_words):
                    self.logger.info(
                        "Message from %s contains blocked words. Skipping.", sender,
                    )
                    return

                if any(content.startswith(group) for group in self.js8groups):
                    for group in self.js8groups:
                        if content.startswith(group):
                            message = content[len(group):].strip()
                            self.forward_group_message(sender, group, message)
                            break
                elif any(content.startswith(group) for group in self.js8urgent):
                    for group in self.js8urgent:
                        if content.startswith(group):
                            message = content[len(group):].strip()
                            self.forward_urgent_message(sender, group, message)
                            break
                else:
                    self.forward_direct_message(sender, content)

        except (KeyError, ValueError) as e:
            self.logger.error("Error handling JS8Call message: %s", e)

    def forward_direct_message(self, sender: str, message: str):
        """Forward a direct message to all LXMF users."""
        formatted_message = f"Direct message from {sender}: {message}"
        self._send_to_users(formatted_message)
        self.db.insert_message(sender, "DIRECT", message)
        self.logger.info("Forwarded direct message from %s", sender)

    def forward_group_message(self, sender: str, group: str, message: str):
        """Forward a group message to subscribed LXMF users."""
        formatted_message = f"Group message from {sender} to {group}: {message}"
        self._send_to_users(formatted_message, group)
        self.db.insert_message(sender, group, message)
        self.logger.info("Forwarded group message from %s to %s", sender, group)

    def forward_urgent_message(self, sender: str, group: str, message: str):
        """Forward an urgent message to subscribed LXMF users."""
        formatted_message = f"URGENT message from {sender} to {group}: {message}"
        self._send_to_users(formatted_message, group)
        self.db.insert_message(sender, group, message)
        self.logger.info("Forwarded urgent message from %s to %s", sender, group)

    def _send_to_users(self, message: str, group: str = None):
        """Send a message to all users or group subscribers.
        If group is None, send to all users. Otherwise, send to users subscribed to the group and not muted.
        """
        for user in self.distro_list:
            if group is None or (
                group in self.user_groups[user] and group not in self.muted_users[user]
            ):
                self.bot.send(user, message, lxmf_fields=self.icon_lxmf_field)

    def show_groups(self, user):
        """Show available groups and user's subscriptions."""
        available_groups = set(self.js8groups + self.js8urgent)
        user_groups = self.user_groups.get(user, set())
        muted_groups = self.muted_users.get(user, set())

        output = "Available groups:\n"
        for group in available_groups:
            status = "[Subscribed]" if group in user_groups else "[Not subscribed]"
            if group in muted_groups:
                status += " [Muted]"
            output += f"{group} {status}\n"
        return output

    def show_info(self):
        """Show bot information."""
        uptime = str(timedelta(seconds=int(time.time() - self.start_time)))
        info = f"Bot uptime: {uptime}\n"
        if self.bot_location:
            info += f"Location: {self.bot_location}\n"
        if self.node_operator:
            info += f"Node operator: {self.node_operator}\n"
        if not self.bot_location and not self.node_operator:
            info += "No additional info available"
        return info

    def show_log(self, num_messages):
        """Show recent messages."""
        num_messages = min(int(num_messages), 50)
        messages = self.execute_db_query(
            """
            SELECT sender, receiver, message, timestamp
            FROM (
                SELECT sender, receiver, message, timestamp FROM messages
                UNION ALL
                SELECT sender, groupname as receiver, message, timestamp FROM groups
                UNION ALL
                SELECT sender, groupname as receiver, message, timestamp FROM urgent
            )
            ORDER BY timestamp DESC
            LIMIT ?
        """,
            (num_messages,),
        )

        log_output = f"Last {len(messages)} messages:\n\n"
        for msg in reversed(messages):
            log_output += f"[{msg[3]}] From {msg[0]} to {msg[1]}: {msg[2]}\n\n"
        return log_output

    def show_stats(self, period=None):
        """Show statistics for the specified period."""
        current_users = len(self.distro_list)
        output = f"Current users: {current_users}\n"

        if period == "day":
            date = datetime.now().strftime("%Y-%m-%d")
            stats = self.execute_db_query(
                "SELECT user_count FROM stats WHERE date = ?", (date,),
            )
            if stats:
                output += f"Users today: {stats[0][0]}\n"
            else:
                output += "No data for today\n"
        elif period == "month":
            current_month = datetime.now().strftime("%Y-%m")
            stats = self.execute_db_query(
                "SELECT AVG(user_count) FROM stats WHERE date LIKE ?",
                (f"{current_month}%",),
            )
            if stats and stats[0][0] is not None:
                avg_users = round(stats[0][0], 2)
                output += f"Average users this month: {avg_users}\n"
            else:
                output += "No data for this month\n"

        return output

    def show_analytics(self, period=None):
        """Show usage statistics for the specified period."""
        output = "Usage Statistics:\n"
        if period == "day":
            date = datetime.now().strftime("%Y-%m-%d")
            messages_count = self.execute_db_query(
                "SELECT COUNT(*) FROM messages WHERE DATE(timestamp) = ?", (date,),
            )
            groups_count = self.execute_db_query(
                "SELECT COUNT(*) FROM groups WHERE DATE(timestamp) = ?", (date,),
            )
            urgent_count = self.execute_db_query(
                "SELECT COUNT(*) FROM urgent WHERE DATE(timestamp) = ?", (date,),
            )
            output += f"Messages today: {messages_count[0][0] if messages_count else 0}\n"
            output += f"Group messages today: {groups_count[0][0] if groups_count else 0}\n"
            output += f"Urgent messages today: {urgent_count[0][0] if urgent_count else 0}\n"
        elif period == "week":
            start_of_week = (datetime.now() - timedelta(days=datetime.now().weekday())).strftime("%Y-%m-%d")
            end_of_week = (datetime.now() + timedelta(days=(6 - datetime.now().weekday()))).strftime("%Y-%m-%d")
            messages_count = self.execute_db_query(
                "SELECT COUNT(*) FROM messages WHERE DATE(timestamp) BETWEEN ? AND ?", (start_of_week, end_of_week),
            )
            groups_count = self.execute_db_query(
                "SELECT COUNT(*) FROM groups WHERE DATE(timestamp) BETWEEN ? AND ?", (start_of_week, end_of_week),
            )
            urgent_count = self.execute_db_query(
                "SELECT COUNT(*) FROM urgent WHERE DATE(timestamp) BETWEEN ? AND ?", (start_of_week, end_of_week),
            )
            output += f"Messages this week: {messages_count[0][0] if messages_count else 0}\n"
            output += f"Group messages this week: {groups_count[0][0] if groups_count else 0}\n"
            output += f"Urgent messages this week: {urgent_count[0][0] if urgent_count else 0}\n"
        else:
            total_messages = self.execute_db_query("SELECT COUNT(*) FROM messages")
            total_groups = self.execute_db_query("SELECT COUNT(*) FROM groups")
            total_urgent = self.execute_db_query("SELECT COUNT(*) FROM urgent")
            output += f"Total direct messages: {total_messages[0][0] if total_messages else 0}\n"
            output += f"Total group messages: {total_groups[0][0] if total_groups else 0}\n"
            output += f"Total urgent messages: {total_urgent[0][0] if total_urgent else 0}\n"
        return output


def main():
    """Entry point for running the JS8CallBot."""
    bot = JS8CallBot()
    bot.run()

if __name__ == "__main__":
    main()
