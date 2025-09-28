cmake --build .
conan list = pip list
conan info .


使用以下方式进行server 和测试 配置对应测试环境 
uv run pytest -s tests/test_main.py::test_get_id_from_name 
uv run python -m clientz.server 80 --prod

docker-compose build --no-cache
