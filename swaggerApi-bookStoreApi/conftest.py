"""
 configure the url argument
"""

def pytest_addoption(parser):
    parser.addoption("--url",action="store",default="https://bookstore.toolsqa.com/")