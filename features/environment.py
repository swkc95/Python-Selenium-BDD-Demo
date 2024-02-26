from behave import fixture
from behave.fixture import use_fixture
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from fixtures.driver import get_local_driver
from lib.misc.string_importer import import_string_file
import lib.misc.variables as v


def before_all(context):
    context.retries = context.config.userdata.getint("retries", 0)
    context.headless = context.config.userdata.getbool("headless", True)
    context.debug = context.config.userdata.getbool("debug", False)
    # context.language = context.config.userdata.get("language", "english")
    # context.runner_mode = context.config.userdata.get("runner_mode", "local")
    # context.used_browser = context.config.userdata.get("browser", "chrome")
    context.language = "english"
    context.runner_mode = "local"
    context.used_browser = "chrome"
    context.strings = import_string_file(context.language)


def before_feature(context, feature):
    if context.retries > 0:
        for scenario in feature.scenarios:
            patch_scenario_with_autoretry(scenario, max_attempts=context.retries+1)


def before_scenario(context, scenario):
    context.info_banner_flag = True


@fixture
def browser_fixture(context):
    if context.runner_mode == "local":
        context.browser = get_local_driver(context)
        context.browser.maximize_window()
        yield context.browser
    # else:
    #     if context.runner_mode == "cicd":
    #         exec_url = v.CICD_URL
    #     elif context.runner_mode == "grid":
    #         exec_url = v.GRID_URL
    #     else:
    #         return ValueError("Invalid runner_mode")
    #     context.browser = get_remote_driver(context, exec_url)
    #     yield context.browser
    #     context.browser.quit()


def before_tag(context, tag):
    if tag == "fixture.browser":
        use_fixture(browser_fixture, context)


def after_step(context, step):
    if step.status == 'failed':
        context.failed_step = step.name


def after_scenario(context, scenario):
    if scenario.status == 'failed' and hasattr(context, "browser"):
        filename = rf"{context.evidence_path}\screenshot.png"
        # if context.runner_mode == "cicd":
        #     filename = filename.replace("\\", "/")
        context.browser.save_screenshot(filename)
