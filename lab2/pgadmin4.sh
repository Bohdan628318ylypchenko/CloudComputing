docker run -p 80:80 \
    --network lab2_lab2 \
    -e PGADMIN_DEFAULT_EMAIL=bp@kv41mn.com \
    -e PGADMIN_DEFAULT_PASSWORD=123 \
    -e PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION=True \
    -e PGADMIN_CONFIG_CONSOLE_LOG_LEVEL=10 \
    dpage/pgadmin4
