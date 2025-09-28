use crate::evaluate_type::{
    stmt::get_variable_types,
    types::{PredefinedTypes, Type},
    JinjaContext,
};

macro_rules! assert_evaluates_to {
    ($expr:expr, $types:expr) => {{
        let parsed = minijinja::machinery::parse(
            $expr,
            "prompt",
            minijinja::syntax::SyntaxConfig::default(),
            // TODO: this is not entirely great, but good enough for this use case.
            Default::default(),
        );
        assert!(parsed.is_ok(), "Failed to parse template: {:?}", parsed);
        let parsed = parsed.unwrap();

        let result = get_variable_types(&parsed, &mut $types);
        assert!(
            result.is_empty(),
            "Failed to evaluate expression: {:?}",
            result
        );
    }};
}

macro_rules! assert_fails_to {
    ($expr:expr, $types:expr, $expected:expr) => {{
        let parsed = minijinja::machinery::parse(
            $expr,
            "prompt",
            minijinja::syntax::SyntaxConfig::default(),
            // TODO: this is not entirely great, but good enough for this use case.
            Default::default(),
        );
        assert!(parsed.is_ok(), "Failed to parse template: {:?}", parsed);
        let parsed = parsed.unwrap();

        let result = get_variable_types(&parsed, &mut $types);
        assert!(
            !result.is_empty(),
            "Expected evaluation to fail, but got: {:?}",
            result
        );
        assert_eq!(
            result.iter().map(|x| x.message.clone()).collect::<Vec<_>>(),
            $expected
        );
    }};
}

#[test]
fn evaluate_undefined() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    assert_fails_to!(
        r#"
        {{ prompt }}
        "#,
        types,
        vec!["Variable `prompt` does not exist. Did you mean one of these: `_`, `ctx`?"]
    );
}

#[test]
fn evaluate_number() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    assert_evaluates_to!(
        r#"
        {%- set prompt = 1.1 + 1 -%}
        {{ prompt }}
        "#,
        types
    );
}

#[test]
fn evaluate_bool() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    assert_evaluates_to!(
        r#"
        {%- set prompt = false -%}
        {{ prompt }}
        "#,
        types
    );
}

#[test]
fn evaluate_string() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    assert_evaluates_to!(
        r#"
        {%- set prompt = "hello" -%}
        {{ prompt }}
        "#,
        types
    );
}

#[test]
fn evaluate_pre_vars() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_variable("prompt", Type::Bool);
    assert_evaluates_to!(
        r#"
        {{ prompt }}
        "#,
        types
    );
}

#[test]
fn function_call() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_variable("prompt", Type::Bool);
    assert_fails_to!(
        r#"
        {{ prompt() }}
        "#,
        types,
        vec!["'prompt' is a bool, expected function"]
    );
}

#[test]
fn function_call_1() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_function("prompt", Type::Bool, vec![]);
    assert_evaluates_to!(
        r#"
        {{ prompt() }}
        "#,
        types
    );
}

#[test]
fn function_call_2() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_function("prompt", Type::Bool, vec![("arg".into(), Type::String)]);
    assert_fails_to!(
        r#"
        {% for x in items %}
            {{ prompt(x) }}
        {% endfor %}
        "#,
        types,
        vec!["Variable `items` does not exist. Did you mean one of these: `_`, `ctx`?"]
    );
}

#[test]
fn function_call_3() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_function("prompt", Type::Bool, vec![("arg".into(), Type::String)]);
    types.add_variable("items", Type::List(Box::new(Type::String)));
    assert_evaluates_to!(
        r#"
        {% for x in items %}
            {{ prompt(x) }}
        {% endfor %}
        "#,
        types
    );

    assert_fails_to!(
        r#"
        {% for x in items %}
            {{ prompt(x) }}
        {% endfor %}
        {{ x }}
        "#,
        types,
        vec!["Variable `x` does not exist. Did you mean one of these: `_`, `ctx`, `items`?"]
    );
}

#[test]
fn function_call_4() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_function("prompt", Type::Bool, vec![("arg".into(), Type::String)]);
    types.add_variable(
        "dict_item",
        Type::Map(Box::new(Type::Number), Box::new(Type::String)),
    );
    assert_evaluates_to!(
        r#"
{% for key, value in dict_item|items %}
    Key: {{key}}
    {{ prompt(value) }}
{% else %}
    No items
{% endfor %}
        "#
        .trim(),
        types
    );
}

#[test]
fn loop_builtin() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_variable("items", Type::List(Box::new(Type::String)));
    assert_fails_to!(
        r#"
{% for x in items %}
   {{ loop.a.b }}
   {{ x }}
{% endfor %}
        "#
        .trim(),
        types,
        vec!["class jinja::loop (loop) does not have a property 'a'",]
    );

    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_variable("items", Type::List(Box::new(Type::String)));
    assert_evaluates_to!(
        r#"
{% for x in items %}
   {{ loop.first }}
   {{ x }}
{% endfor %}
        "#
        .trim(),
        types
    );
}

#[test]
fn if_else() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_variable("prompt", Type::String);
    types.add_function("Foo", Type::Bool, vec![("arg".into(), Type::String)]);
    assert_fails_to!(
        r#"
{% if prompt == 'a' -%}
    {% set x = 1 %}
{%- elif prompt == 'abc' -%}
    {% set x = '2' %}
{%- else -%}
  {% set y = '[1]' %}
{%- endif %}
    {{ Foo(x) }}
        "#
        .trim(),
        types,
        vec![
            r#"Function 'Foo' expects argument 'arg' to be of type string, but got (undefined | literal["2"] | literal[1])"#
        ]
    );

    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_variable("prompt", Type::String);
    types.add_function("Foo", Type::Bool, vec![("arg".into(), Type::String)]);
    assert_evaluates_to!(
        r#"
{% if prompt == 'a' -%}
    {% set x = '1' %}
{%- elif prompt == 'abc' -%}
    {% set x = '2' %}
{%- else -%}
  {% set x = '[1]' %}
{%- endif %}
    {{ Foo(x) }}
        "#
        .trim(),
        types
    );
}

#[test]
fn function_reference_without_call_in_template() {
    let mut types = PredefinedTypes::default(JinjaContext::Prompt);
    types.add_function("MyTemplateString", Type::String, vec![]);
    assert_fails_to!(
        r#"
{{ MyTemplateString }}
"#
        .trim(),
        types,
        vec!["Function 'MyTemplateString' referenced without parentheses. Did you mean 'MyTemplateString()'?".to_string()]
    );
}
