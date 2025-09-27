from datetime import datetime, timedelta

import pytest

data = {
    "passed": 0,
    "failed": 0,
}


# 增加配置项
def pytest_addoption(parser):
    parser.addini("send_when", help="发送时间")  # pytest.ini 配置文件中
    parser.addini("send_api", help="发送地址")


# 用例结果
def pytest_runtest_logreport(report: pytest.TestReport):
    if report.when == "call":
        print(f"用例结果为 {report.outcome}")
        data[report.outcome] += 1


# 用例总数
def pytest_collection_finish(session: pytest.Session):
    data["total"] = len(session.items)
    print(f"用例总数：{data['total']}")


# pytest 开始
def pytest_configure(config: pytest.Config):
    data["start_time"] = datetime.now()
    data["send_when"] = config.getini("send_when")
    data["send_api"] = config.getini("send_api")
    print(f"{datetime.now()} pytest 开始执行")


# pytest 结束
def pytest_unconfigure():
    data["end_time"] = datetime.now()
    print(f"{datetime.now()} pytest 结束执行")

    data["duration"] = data["end_time"] - data["start_time"]
    data["passed_ratio"] = (
        data["passed"] / data["total"] * 100 if data["total"] != 0 else 0
    )

    if data["send_api"]:
        if data["send_when"] == "every":
            data["send_done"] = 1

    # assert (
    #     timedelta(seconds=2.5) > data["duration"] > timedelta(seconds=2)
    # )  # 判断执行时间
    # assert data["total"] == 2  # 判断用例数量
    # assert data["passed"] == 2  # 判断执行结果
    # assert data["failed"] == 0

    # print(f"通过率为：{data['passed_ratio']:.2f}%")
