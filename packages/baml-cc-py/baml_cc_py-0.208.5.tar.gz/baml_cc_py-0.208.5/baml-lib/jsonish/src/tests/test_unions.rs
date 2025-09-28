use baml_types::{ir_type::UnionConstructor, type_meta::base::TypeMeta};

use super::*;

//
const FOO_FILE: &str = r#"
class Foo {
  hi string[]
}

class Bar {
  foo string
}
"#;

test_deserializer!(
  test_union,
  FOO_FILE,
  r#"{"hi": ["a", "b"]}"#,
  TypeIR::union(vec![TypeIR::class("Foo"), TypeIR::class("Bar")]),
  {"hi": ["a", "b"]}
);

#[test_log::test]
fn test_union_full() {
    let ir = crate::helpers::load_test_ir(FOO_FILE);
    let target_type = TypeIR::union(vec![TypeIR::class("Foo"), TypeIR::class("Bar").as_list()]);
    let target = crate::helpers::render_output_format(
        &ir,
        &target_type,
        &Default::default(),
        baml_types::StreamingMode::NonStreaming,
    )
    .unwrap();

    let result = from_str(&target, &target_type, r#"{"hi": ["a", "b"]}"#, true);

    assert!(result.is_ok(), "Failed to parse: {result:?}");

    let value = result.unwrap();
    log::trace!("Score: {}", value.score());
    assert_eq!(value.field_type(), &target_type);
    if let BamlValueWithFlags::Class(cls_name, _, cls_type, props) = &value {
        for (prop_name, prop_value) in props {
            match prop_name.as_str() {
                "hi" => {
                    let mut item_type = TypeIR::Primitive(TypeValue::String, TypeMeta::default());
                    item_type.meta_mut().streaming_behavior.needed = true;
                    let mut target_type = item_type.as_list();
                    target_type.meta_mut().streaming_behavior.needed = true;
                    assert_eq!(
                        prop_value.field_type(),
                        &target_type,
                        "{} != {target_type}",
                        prop_value.field_type()
                    );

                    let item_type = match &target_type {
                        TypeIR::List(item, _) => item.as_ref(),
                        _ => panic!("Expected a list"),
                    };
                    for item in prop_value.as_list().unwrap() {
                        assert_eq!(item.field_type(), item_type);
                    }
                }
                _ => {
                    panic!("Unexpected property: {prop_name}");
                }
            }
        }
    } else {
        panic!("Expected a class");
    }
    let value: BamlValue = value.into();
    log::info!("{value}");
    let json_value = json!(value);

    let expected = serde_json::json!({"hi": ["a", "b"]});

    assert_json_diff::assert_json_eq!(json_value, expected);
}

const SPUR_FILE: &str = r###"
enum CatA {
  A
}

enum CatB {
  C
  D
}

class CatAPicker {
  cat CatA
}

class CatBPicker {
  cat CatB
  item int
}

enum CatC {
  E
  F 
  G 
  H 
  I
}

class CatCPicker {
  cat CatC
  item  int | string | null
  data int?
}
"###;

test_deserializer!(
  test_union2,
  SPUR_FILE,
  r#"```json
  {
    "cat": "E",
    "item": "28558C",
    "data": null
  }
  ```"#,
  TypeIR::union(vec![TypeIR::class("CatAPicker"), TypeIR::class("CatBPicker"), TypeIR::class("CatCPicker")]),
  {
    "cat": "E",
    "item": "28558C",
    "data": null
  }
);

const CUSTOMER_FILE2: &str = r###"
enum AssistantType {
  ETF @alias("ETFAssistantAPI")
  Stock @alias("StockAssistantAPI")
}

class AssistantAPI {
  action AssistantType
  instruction string @description("Detailed instructions for the assistants API to be able to process the request")
  user_message string @description("The message to keep the user informed")

  @@description(#"
    Used for 
  "#)
}

enum AskClarificationAction {
  ASK_CLARIFICATION @alias("AskClarificationAPI")
}

class AskClarificationAPI {
  action AskClarificationAction
  question string @description("The clarification question to ask the user")
}

enum RespondToUserAction {
  RESPOND_TO_USER @alias("RespondToUserAPI")
}

class RespondToUserAPI {
  action RespondToUserAction
  sections UI[]
}

class Message {
  role string
  message string
}



enum UIType {
  CompanyBadge @description("Company badge UI type")
  Markdown @description("Markdown text UI type")
  NumericalSlider @description("Numerical slider UI type")
  BarGraph @description("Bar graph UI type")
  ScatterPlot @description("Scatter plot UI type")
}

class MarkdownContent {
  text string
}

class CompanyBadgeContent {
  name string
  symbol string
  logo_url string
}

class NumericalSliderContent {
  title string
  min float
  max float
  value float
}

class TabContent {
  title string
  content string
}

class GraphDataPoint {
  name string
  expected float
  reported float
}

class ScatterDataPoint {
  x string
  y float
}

class ScatterPlotContent {
  expected ScatterDataPoint[]
  reported ScatterDataPoint[]
}

class UIContent {
  richText MarkdownContent?
  companyBadge CompanyBadgeContent?
  numericalSlider NumericalSliderContent?
  barGraph GraphDataPoint[] | null
  scatterPlot ScatterPlotContent?
  foo string?
}

class UI {
  section_title string
  type UIType[] @alias(types)
  content UIContent
}

"###;

test_deserializer!(
  test_union3,
  CUSTOMER_FILE2,
  r####"```json
{
  "action": "RespondToUserAPI",
  "sections": [
    {
      "section_title": "NVIDIA Corporation (NVDA) Latest Earnings Summary",
      "types": ["CompanyBadge", "Markdown", "BarGraph"],
      "content": {
        "companyBadge": {
          "name": "NVIDIA Corporation",
          "symbol": "NVDA",
          "logo_url": "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Nvidia_logo.svg/1920px-Nvidia_logo.svg.png"
        },
        "richText": {
          "text": "### Key Metrics for the Latest Earnings Report (2024-08-28)\n\n- **Earnings Per Share (EPS):** $0.68\n- **Estimated EPS:** $0.64\n- **Revenue:** $30.04 billion\n- **Estimated Revenue:** $28.74 billion\n\n#### Notable Highlights\n- NVIDIA exceeded both EPS and revenue estimates for the quarter ending July 28, 2024.\n- The company continues to show strong growth in its data center and gaming segments."
        },
        "barGraph": [
          {
            "name": "Earnings Per Share (EPS)",
            "expected": 0.64,
            "reported": 0.68
          },
          {
            "name": "Revenue (in billions)",
            "expected": 28.74,
            "reported": 30.04
          }
        ]
      }
    }
  ]
}
```"####,
  TypeIR::union(vec![TypeIR::class("RespondToUserAPI"), TypeIR::class("AskClarificationAPI"), TypeIR::class("AssistantAPI").as_list()]),
  {
    "action": "RESPOND_TO_USER",
    "sections": [
      {
        "section_title": "NVIDIA Corporation (NVDA) Latest Earnings Summary",
        "type": ["CompanyBadge", "Markdown", "BarGraph"],
        "content": {
          "companyBadge": {
            "name": "NVIDIA Corporation",
            "symbol": "NVDA",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Nvidia_logo.svg/1920px-Nvidia_logo.svg.png"
          },
          "richText": {
            "text": "### Key Metrics for the Latest Earnings Report (2024-08-28)\n\n- **Earnings Per Share (EPS):** $0.68\n- **Estimated EPS:** $0.64\n- **Revenue:** $30.04 billion\n- **Estimated Revenue:** $28.74 billion\n\n#### Notable Highlights\n- NVIDIA exceeded both EPS and revenue estimates for the quarter ending July 28, 2024.\n- The company continues to show strong growth in its data center and gaming segments."
          },
          "scatterPlot": null,
          "numericalSlider": null,
          "barGraph": [
            {
              "name": "Earnings Per Share (EPS)",
              "expected": 0.64,
              "reported": 0.68
            },
            {
              "name": "Revenue (in billions)",
              "expected": 28.74,
              "reported": 30.04
            }
          ],
          "foo": null
        }
      }
    ]
  }
);

const CONTACT_INFO: &str = r#"
class PhoneNumber {
  value string @check(valid_phone_number, {{this|regex_match("\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")}})
}

class EmailAddress {
  value string @check(valid_email, {{this|regex_match("^[_]*([a-z0-9]+(\.|_*)?)+@([a-z][a-z0-9-]+(\.|-*\.))+[a-z]{2,6}$")}})
}

class ContactInfo {
  primary PhoneNumber | EmailAddress
}
"#;

test_deserializer!(
  test_phone_number_regex,
  CONTACT_INFO,
  r#"{"primary": {"value": "908-797-8281"}}"#,
  TypeIR::class("ContactInfo"),
  {"primary": {"value": "908-797-8281"}}
);

test_deserializer!(
  test_email_regex,
  CONTACT_INFO,
  r#"{"primary": {"value": "help@boundaryml.com"}}"#,
  TypeIR::class("ContactInfo"),
  {"primary": {"value": "help@boundaryml.com"}}
);

test_deserializer!(
    test_ignore_float_in_string_if_string_in_union,
    "",
    "1 cup unsalted butter, room temperature",
    TypeIR::union(vec![
        TypeIR::Primitive(TypeValue::Float, TypeMeta::default()),
        TypeIR::Primitive(TypeValue::String, TypeMeta::default()),
    ]),
    "1 cup unsalted butter, room temperature"
);

test_deserializer!(
    test_ignore_int_if_string_in_union,
    "",
    "1 cup unsalted butter, room temperature",
    TypeIR::union(vec![
        TypeIR::Primitive(TypeValue::Int, TypeMeta::default()),
        TypeIR::Primitive(TypeValue::String, TypeMeta::default()),
    ]),
    "1 cup unsalted butter, room temperature"
);
