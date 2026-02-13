// This bot is developed by **RETOUCH**
module.exports = {
  apps: [{
    name: "RETOUCH_ELITE",
    script: "bot.py",
    interpreter: "python3",
    restart_delay: 2000,
    max_memory_restart: "500M",
    env: {
      NODE_ENV: "production",
    }
  }]
}
