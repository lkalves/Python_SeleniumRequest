
from behave import fixture, use_fixture
from selenium.webdriver import Chrome

@fixture
def browser_chrome(context):
    context.browser = Chrome()
    yield context.browser
    context.browser.quit()

def before_step(context, step):
    # context.valores[step.name] = 'iniciou'
    ...


def after_step(context, step):
    # context.valores[step.name] = 'finalizou'
    ...

def before_scenario(context, scenario):
    ...


def after_scenario(context, scenario):
    ...


def before_feature(context, feature):
    ...


def after_feature(context, feature):
    ...


def before_all(context):
    use_fixture(browser_chrome, context)


def after_all(context):
    ...
