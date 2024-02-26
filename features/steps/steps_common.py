from behave import step


@step("Admin logs in")
def step_impl(context):
    context.execute_steps(f"""
    Given Admin is on the log in page
    When Admin provides a valid username
    And Admin provides a valid password
    And Admin submits the log in request
    Then Admin is logged in
    """)
