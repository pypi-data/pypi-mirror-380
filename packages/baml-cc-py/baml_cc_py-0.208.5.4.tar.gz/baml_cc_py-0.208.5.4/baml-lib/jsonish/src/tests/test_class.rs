use baml_types::type_meta::base::TypeMeta;

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

// Usage
test_deserializer!(
    test_foo,
    FOO_FILE,
    r#"{"hi": ["a", "b"]}"#,
    TypeIR::class("Foo"),
    {"hi": ["a", "b"]}
);

test_deserializer!(
    test_wrapped_objects,
    FOO_FILE,
    r#"{"hi": "a"}"#,
    TypeIR::list(TypeIR::class("Foo")),
    [{"hi": ["a"]}]
);

test_deserializer!(
    test_string_from_obj_and_string,
    FOO_FILE,
    r#"The output is: {"hi": ["a", "b"]}"#,
    TypeIR::class("Foo"),
    {"hi": ["a", "b"]}
);

test_deserializer!(
    test_string_from_obj_and_string_with_extra_text,
    FOO_FILE,
    r#"This is a test. The output is: {"hi": ["a", "b"]}"#,
    TypeIR::class("Foo"),
    {"hi": ["a", "b"]}
);

test_deserializer!(
    test_string_from_obj_and_string_with_invalid_extra_text,
    FOO_FILE,
    r#"{"hi": ["a", "b"]} is the output."#,
    TypeIR::class("Foo"),
    {"hi": ["a", "b"]}
);

test_deserializer!(
  str_with_quotes,
  FOO_FILE,
  r#"{"foo": "[\"bar\"]"}"#,
  TypeIR::class("Bar"),
  {"foo": "[\"bar\"]"}
);

test_deserializer!(
  str_with_nested_json,
  FOO_FILE,
  r#"{"foo": "{\"foo\": [\"bar\"]}"}"#,
  TypeIR::class("Bar"),
  {"foo": "{\"foo\": [\"bar\"]}"}
);

test_deserializer!(
    test_obj_from_str_with_string_foo,
    FOO_FILE,
    r#"
{  
  "foo": "Here is how you can build the API call:\n```json\n{\n  \"foo\": {\n    \"world\": [\n      \"bar\"\n    ]\n  }\n}\n```"
}
"#,
    TypeIR::class("Bar"),
    {"foo": "Here is how you can build the API call:\n```json\n{\n  \"foo\": {\n    \"world\": [\n      \"bar\"\n    ]\n  }\n}\n```"}
);

const OPTIONAL_FOO: &str = r#"
class Foo {
  foo string?
}
"#;

test_deserializer!(
    test_optional_foo,
    OPTIONAL_FOO,
    r#"{}"#,
    TypeIR::class("Foo"),
    { "foo": null }
);

test_deserializer!(
    test_optional_foo_with_value,
    OPTIONAL_FOO,
    r#"{"foo": ""}"#,
    TypeIR::class("Foo"),
    { "foo": "" }
);

const MULTI_FIELDED_FOO: &str = r#"
class Foo {
  one string
  two string?
}
"#;

test_deserializer!(
    test_multi_fielded_foo,
    MULTI_FIELDED_FOO,
    r#"{"one": "a"}"#,
    TypeIR::class("Foo"),
    { "one": "a", "two": null }
);

test_deserializer!(
    test_multi_fielded_foo_with_optional,
    MULTI_FIELDED_FOO,
    r#"{"one": "a", "two": "b"}"#,
    TypeIR::class("Foo"),
    { "one": "a", "two": "b" }
);

test_deserializer!(
    test_multi_fielded_foo_with_optional_and_extra_text,
    MULTI_FIELDED_FOO,
    r#"Here is how you can build the API call:
    ```json
    {
        "one": "hi",
        "two": "hello"
    }
    ```
    
    ```json
        {
            "test2": {
                "key2": "value"
            },
            "test21": [
            ]    
        }
    ```"#,
    TypeIR::class("Foo"),
    { "one": "hi", "two": "hello" }
);

const MULTI_FIELDED_FOO_WITH_LIST: &str = r#"
class Foo {
  a int
  b string
  c string[]
}
"#;

test_deserializer!(
    test_multi_fielded_foo_with_list,
    MULTI_FIELDED_FOO_WITH_LIST,
    r#"{"a": 1, "b": "hi", "c": ["a", "b"]}"#,
    TypeIR::class("Foo"),
    { "a": 1, "b": "hi", "c": ["a", "b"] }
);

const NEST_CLASS: &str = r#"
class Foo {
  a string
}

class Bar {
  foo Foo
}
"#;

test_deserializer!(
    test_nested_class,
    NEST_CLASS,
    r#"{"foo": {"a": "hi"}}"#,
    TypeIR::class("Bar"),
    { "foo": { "a": "hi" } }
);

test_deserializer!(
    test_nested_class_with_extra_text,
    NEST_CLASS,
    r#"Here is how you can build the API call:
    ```json
    {
        "foo": {
            "a": "hi"
        }
    }
    ```
    
    and this
    ```json
    {
        "foo": {
            "a": "twooo"
        }
    }"#,
    TypeIR::class("Bar"),
    { "foo": { "a": "hi" } }
);

test_deserializer!(
    test_nested_class_with_prefix,
    NEST_CLASS,
    r#"Here is how you can build the API call:
    {
        "foo": {
            "a": "hi"
        }
    }
    
    and this
    {
        "foo": {
            "a": "twooo"
        }
    }
    "#,
    TypeIR::class("Bar"),
    { "foo": { "a": "hi" } }
);

const NEST_CLASS_WITH_LIST: &str = r#"
class Resume {
    name string
    email string?
    phone string?
    experience string[] 
    education string[] 
    skills string[] 
    
    @@stream.not_null
}
"#;

test_deserializer!(
    test_resume,
    NEST_CLASS_WITH_LIST,
    r#"{
        "name": "Lee Hsien Loong",
        "email": null,
        "phone": null,
        "experience": [
            "Senior Minister of Singapore since 2024",
            "Prime Minister of Singapore from 2004 to 2024",
            "Member of Parliament (MP) for the Teck Ghee division of Ang Mo Kio GRC since 1991",
            "Teck Ghee SMC between 1984 and 1991",
            "Secretary-General of the People's Action Party (PAP) since 2004"
        ],
        "education": [],
        "skills": ["politician", "former brigadier-general"]
    }"#,
    TypeIR::class("Resume"),
    {
        "name": "Lee Hsien Loong",
        "email": null,
        "phone": null,
        "experience": [
            "Senior Minister of Singapore since 2024",
            "Prime Minister of Singapore from 2004 to 2024",
            "Member of Parliament (MP) for the Teck Ghee division of Ang Mo Kio GRC since 1991",
            "Teck Ghee SMC between 1984 and 1991",
            "Secretary-General of the People's Action Party (PAP) since 2004"
        ],
        "education": [],
        "skills": ["politician", "former brigadier-general"]
    }
);

test_partial_deserializer!(
    test_resume_partial,
    NEST_CLASS_WITH_LIST,
    r#"{
        "name": "Lee Hsien Loong",
        "email": null,
        "phone": null,
        "experience": [
            "Senior Minister of Singapore since 2024",
            "Prime Minister of Singapore from 2004 to "#,
    TypeIR::class("Resume"),
    {
        "name": "Lee Hsien Loong",
        "email": null,
        "phone": null,
        "experience": [
            "Senior Minister of Singapore since 2024",
            "Prime Minister of Singapore from 2004 to "
        ],
        "education": [],
        "skills": []
    }
);

test_partial_deserializer!(
    test_resume_partial_2,
    NEST_CLASS_WITH_LIST,
    r#"{
        "experience": [
            "Senior Minister of Singapore since 2024",
            "Prime Minister of Singapore from 2004 to "#,
    TypeIR::class("Resume"),
    {
        "name": null,
        "email": null,
        "phone": null,
        "experience": [
            "Senior Minister of Singapore since 2024",
            "Prime Minister of Singapore from 2004 to "
        ],
        "education": [],
        "skills": []
    }
);

const CLASS_WITH_ALIASES: &str = r#"
class TestClassAlias {
    key string @alias("key-dash")
    key2 string @alias("key21")
    key3 string @alias("key with space")
    key4 string //unaliased
    key5 string @alias("key.with.punctuation/123")
}
"#;

test_deserializer!(
    test_aliases,
    CLASS_WITH_ALIASES,
    r#"{
        "key-dash": "This is a value with a dash",
        "key21": "This is a value for key21",
        "key with space": "This is a value with space",
        "key4": "This is a value for key4",
        "key.with.punctuation/123": "This is a value with punctuation and numbers"
      }"#,
    TypeIR::class("TestClassAlias"),
    {
        "key": "This is a value with a dash",
        "key2": "This is a value for key21",
        "key3": "This is a value with space",
        "key4": "This is a value for key4",
        "key5": "This is a value with punctuation and numbers"
    }
);

const CLASS_SIMPLE: &str = r#"
class SimpleTest {
    answer Answer
}
  
class Answer {
    content float
}
"#;

test_deserializer!(
    test_class_with_whitespace_keys,
    CLASS_SIMPLE,
    r#"{" answer ": {" content ": 78.54}}"#,
    TypeIR::class("SimpleTest"),
    {
        "answer": {
            "content": 78.54
        }
    }
);

const CLASS_WITH_NESTED_CLASS_LIST: &str = r#"
class Resume {
    name string
    education Education[]
    skills string[]
  }
  
  class Education {
    school string
    degree string
    year int
  }
"#;

test_deserializer!(
    test_class_with_nested_list,
    CLASS_WITH_NESTED_CLASS_LIST,
    r#"{
        "name": "Vaibhav Gupta",
        "education": [
            {
                "school": "FOOO",
                "degree": "FOOO",
                "year": 2015
            },
            {
                "school": "BAAR",
                "degree": "BAAR",
                "year": 2019
            }
        ],
        "skills": [
          "C++",
          "SIMD on custom silicon"
        ]
      }"#,
    TypeIR::class("Resume"),
    {
        "name": "Vaibhav Gupta",
        "education": [
            {
                "school": "FOOO",
                "degree": "FOOO",
                "year": 2015
            },
            {
                "school": "BAAR",
                "degree": "BAAR",
                "year": 2019
            }
        ],
        "skills": [
            "C++",
            "SIMD on custom silicon"
        ]
    }
);

test_deserializer!(
    test_class_with_nestedd_list_just_list,
    CLASS_WITH_NESTED_CLASS_LIST,
    r#"[
          {
            "school": "FOOO",
            "degree": "FOOO",
            "year": 2015
          },
          {
            "school": "BAAR",
            "degree": "BAAR",
            "year": 2019
          }
        ]
    "#,
    TypeIR::list(TypeIR::class("Education")),
        [
            {
                "school": "FOOO",
                "degree": "FOOO",
                "year": 2015
            },
            {
                "school": "BAAR",
                "degree": "BAAR",
                "year": 2019
            }
        ]
);

const FUNCTION_FILE: &str = r#"
class Function {
    selected (Function1 | Function2 | Function3)
}

class Function1 {
    function_name string
    radius int
}

class Function2 {
    function_name string
    diameter int
}

class Function3 {
    function_name string
    length int
    breadth int
}
"#;

test_deserializer!(
    test_obj_created_when_not_present,
    FUNCTION_FILE,
    r#"[
        {
          // Calculate the area of a circle based on the radius.
          function_name: 'circle.calculate_area',
          // The radius of the circle.
          radius: 5,
        },
        {
          // Calculate the circumference of a circle based on the diameter.
          function_name: 'circle.calculate_circumference',
          // The diameter of the circle.
          diameter: 10,
        }
      ]"#,
    TypeIR::list(TypeIR::class("Function")),
    [
        {"selected": {
            "function_name": "circle.calculate_area",
            "radius": 5
        },
    },
        {"selected":
        {
            "function_name": "circle.calculate_circumference",
            "diameter": 10
        }
        }
    ]
);

test_deserializer!(
    test_trailing_comma_with_space_last_field,
    FUNCTION_FILE,
    r#"
    {
      // Calculate the circumference of a circle based on the diameter.
      function_name: 'circle.calculate_circumference',
      // The diameter of the circle. (with a ", ")
      diameter: 10, 
    }
    "#,
    TypeIR::class("Function2"),
    {
        "function_name": "circle.calculate_circumference",
        "diameter": 10
    }
);

test_deserializer!(
    test_trailing_comma_with_space_last_field_and_extra_text,
    FUNCTION_FILE,
    r#"
    {
      // Calculate the circumference of a circle based on the diameter.
      function_name: 'circle.calculate_circumference',
      // The diameter of the circle. (with a ", ")
      diameter: 10, 
      Some key: "Some value"
    }
    and this
    "#,
    TypeIR::class("Function2"),
    {
        "function_name": "circle.calculate_circumference",
        "diameter": 10
    }
);

test_failing_deserializer!(
    test_nested_obj_from_string_fails_0,
    r#"
    class Foo {
        foo Bar
    }

    class Bar {
        bar string
        option int?
    }
    "#,
    r#"My inner string"#,
    TypeIR::class("Foo")
);

test_failing_deserializer!(
    test_nested_obj_from_string_fails_1,
    r#"
    class Foo {
        foo Bar
    }

    class Bar {
        bar string
    }
    "#,
    r#"My inner string"#,
    TypeIR::class("Foo")
);

test_failing_deserializer!(
    test_nested_obj_from_string_fails_2,
    r#"
    class Foo {
        foo string
    }
    "#,
    r#"My inner string"#,
    TypeIR::class("Foo")
);

test_deserializer!(
    test_nested_obj_from_int,
    r#"
    class Foo {
        foo int
    }
    "#,
    r#"1214"#,
    TypeIR::class("Foo"),
    { "foo": 1214 }
);

test_deserializer!(
    test_nested_obj_from_float,
    r#"
    class Foo {
        foo float
    }
    "#,
    r#"1214.123"#,
    TypeIR::class("Foo"),
    { "foo": 1214.123 }
);

test_deserializer!(
    test_nested_obj_from_bool,
    r#"
    class Foo {
        foo bool
    }
    "#,
    r#" true "#,
    TypeIR::class("Foo"),
    { "foo": true }
);

const NESTED_CLASSES: &str = r##"
class Nested {
  prop3 string | null @description(#"
    write "three"
  "#)
  prop4 string | null @description(#"
    write "four"
  "#) @alias("blah")
  prop20 Nested2
}

class Nested2 {
  prop11 string | null @description(#"
    write "three"
  "#)
  prop12 string | null @description(#"
    write "four"
  "#) @alias("blah")
}

class Schema {
  prop1 string | null @description(#"
    write "one"
  "#)
  prop2 Nested | string @description(#"
    write "two"
  "#)
  prop5 (string | null)[] @description(#"
    write "hi"
  "#)
  prop6 string | Nested[] @alias("blah") @description(#"
    write the string "blah" regardless of the other types here
  "#)
  nested_attrs (string | null | Nested)[] @description(#"
    write the string "nested" regardless of other types
  "#)
  parens (string | null) @description(#"
    write "parens1"
  "#)
  other_group (string | (int | string)) @description(#"
    write "other"
  "#) @alias(other)
}
"##;

test_deserializer!(
    test_nested_classes_with_aliases,
    NESTED_CLASSES,
    r#"
```json
{
  "prop1": "one",
  "prop2": {
    "prop3": "three",
    "blah": "four",
    "prop20": {
      "prop11": "three",
      "blah": "four"
    }
  },
  "prop5": ["hi"],
  "blah": "blah",
  "nested_attrs": ["nested"],
  "parens": "parens1",
  "other": "other"
}
```
"#,
TypeIR::class("Schema"),
{
    "prop1": "one",
    "prop2": {
      "prop3": "three",
      "prop4": "four",
      "prop20": {
        "prop11": "three",
        "prop12": "four"
      }
    },
    "prop5": ["hi"],
    "prop6": "blah",
    "nested_attrs": ["nested"],
    "parens": "parens1",
    "other_group": "other"
  }
);

test_deserializer!(
test_ekinsdrow,
r#"

// ------------ Heading 3 ----------------
class Heading3 {
  type Heading3Type @description("Always heading_3")
  heading_3 HeadingBody @description("Heading 3 block with rich text")
}

class HeadingBody {
  rich_text RichText[] @description("The rich text content of the heading")
  is_toggleable bool @description("Whether the heading is toggleable")
}

/// ------------ Paragraph ----------------
class Paragraph {
  type ParagraphType @description("Always paragraph")
  paragraph ParagraphBody @description("Paragraph block with rich text")
}

class ParagraphBody {
  rich_text RichText[] @description("The rich text displayed in the paragraph block")
  children string[] @description("Optional nested child blocks for paragraph")
}

/// ------------ RichText ----------------
class RichText {
  type RichTextType @description("Always text")
  text RichTextContent
}

  class RichTextContent {
    content string @description("The content of the rich text element")
  }

/// ------------ To Do ----------------
class ToDo {
  type ToDoType @description("Always to_do")
  to_do ToDoBody @description("To-do block with checkbox and content")
}

class ToDoBody {
  rich_text RichText[] @description("The text content of the to-do item")
  checked bool? @description("Whether the to-do item is checked")
  children Paragraph[] @description("Optional nested child blocks for to-do")
}

class Page {
    object string @description("Always page")
    icon Icon
    children (Breadcrumb | ColumnList | Heading3 | Paragraph | ToDo)[] @description("Some blocks of the page")
}

// ------------ Breadcrumb ----------------
class Breadcrumb {
  type BreadcrumbType @description("Always breadcrumb")
  breadcrumb map<string, string> @description("Always empty map")
}

// ------------ Breadcrumb ----------------
class Breadcrumb1 {
  type BreadcrumbType @description("Always breadcrumb")
  breadcrumb map<string, string> @description("Always empty map")
}

/// ------------ Column List ----------------
class ColumnList {
  type ColumnListType @description("Always column_list")
  column_list ColumnListBody @description("Column list block with columns")
}

class ColumnListBody {
  children Column[] @description("The columns in the column list. Max length is 5")
}

class Column {
  type ColumnType @description("Always column")
  column ColumnBody @description("Always empty map for columns")
}

class ColumnBody {
  children (Breadcrumb1 | Heading3 | Paragraph | ToDo)[] @description("Content of the column. Can contain any block type. Min length is 1")
}

class Icon {
    emoji string @description("The emoji of the icon")
}

enum ColumnType  {
    Column @alias("column")
}

enum BookmarkType {
    Bookmark @alias("bookmark")
  }
  
  enum BreadcrumbType {
    Breadcrumb @alias("breadcrumb")
  }
  
  enum BulletedListItemType {
    BulletedListItem @alias("bulleted_list_item")
  }
  
  enum CalloutType {
    Callout @alias("callout")
  }
  
  enum CodeType {
    Code @alias("code")
  }
  
  enum ColumnListType {
    ColumnList @alias("column_list")
  }
  
  enum DividerType {
    Divider @alias("divider")
  }
  
  enum EmbedType {
    Embed @alias("embed")
  }
  
  enum EquationType {
    Equation @alias("equation")
  }
  
  enum FileType {
    File @alias("file")
  }
  
  enum Heading1Type {
    Heading1 @alias("heading1")
  }
  
  enum Heading2Type {
    Heading2 @alias("heading2")
  }
  
  enum Heading3Type {
    Heading3 @alias("heading_3")
  }
  
  enum ImageFileType {
    ImageFile @alias("image_file")
  }
  
  enum NumberedListItemType {
    NumberedListItem @alias("numbered_list_item")
  }
  
  enum ParagraphType {
    Paragraph @alias("paragraph")
  }
  
  enum PdfType {
    Pdf @alias("pdf")
  }
  
  enum QuoteType {
    Quote @alias("quote")
  }
  
  enum RichTextType {
    RichText @alias("text")
  }
  
  enum TableType {
    Table @alias("table")
  }
  
  enum TableOfContentsType {
    TableOfContents @alias("table_of_contents")
  }
  
  enum ToDoType {
    ToDo @alias("to_do")
  }
  
  enum ToggleType {
    Toggle @alias("toggle")
  }
  
  enum VideoType {
    Video @alias("video")
  }
    "#,
r#"{
  "object": "page",
  "icon": {
    "emoji": "📚"
  },
  "children": [
    {
      "type": "column_list",
      "column_list": {
        "children": [
          {
            "type": "column",
            "column": {
              "children": [
                {
                  "type": "heading_3",
                  "heading_3": {
                    "rich_text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "The Lord of the Rings"
                        }
                      }
                    ],
                    "is_toggleable": false
                  }
                },
                {
                  "type": "paragraph",
                  "paragraph": {
                    "rich_text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "J.R.R. Tolkien"
                        }
                      }
                    ]
                  }
                },
                {
                  "type": "to_do",
                  "to_do": {
                    "rich_text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "Read again"
                        }
                      }
                    ],
                    "checked": false
                  }
                }
              ]
            }
          }
        ]
      }
    }
  ]
}"#,
TypeIR::class("Page"),
{
    "object": "page",
    "icon": {
      "emoji": "📚"
    },
    "children": [
      {
        "type": "ColumnList",
        "column_list": {
          "children": [
            {
              "type": "Column",
              "column": {
                "children": [
                  {
                    "type": "Heading3",
                    "heading_3": {
                      "rich_text": [
                        {
                          "type": "RichText",
                          "text": {
                            "content": "The Lord of the Rings"
                          }
                        }
                      ],
                      "is_toggleable": false
                    }
                  },
                  {
                    "type": "Paragraph",
                    "paragraph": {
                      "rich_text": [
                        {
                          "type": "RichText",
                          "text": {
                            "content": "J.R.R. Tolkien"
                          }
                        }
                      ],
                    "children": []
                    }
                  },
                  {
                    "type": "ToDo",
                    "to_do": {
                      "rich_text": [
                        {
                          "type": "RichText",
                          "text": {
                            "content": "Read again"
                          }
                        }
                      ],
                      "checked": false,
                    "children": []
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
);

test_deserializer!(
  test_escaped_quotes,
  r#"
class TextSection {
  text string
}

class CodeSection {
  code_language string
  code string
}


class DoCommandACReturnType {
  sections (TextSection | CodeSection)[] @description("The sections of the response. Must choose one of text or code_language+code.")
}
  "#,
  r#"
Certainly! I'll redesign the UI to make it more appealing to a female audience. I'll focus on color schemes, fonts, and imagery that are generally more attractive to women. Here's my thought process and suggestions:
    
Thoughts: "The current design is quite neutral. We can make it more feminine by using softer colors, curved shapes, and adding some playful elements. We should also consider updating the trending items to be more relevant to a female audience."

"We can use a pastel color scheme, which is often associated with femininity. Let's go with a soft pink as the primary color, with accents of lavender and mint green."

"For the font, we can use a more elegant and rounded typeface for the logo and headings. This will give a softer, more feminine look."

"We should update the trending items to include more fashion-focused and accessory items that are popular among women."

Here's the redesigned code with these changes:

{
  "sections": [
    {
      "code_language": "swift",
      "code": "import SwiftUI\n\nstruct ContentView: View {\n    var body: some View {\n        ZStack(alignment: .bottom) {\n            VStack(spacing: 0) {\n                CustomNavigationBar()\n                \n                ScrollView {\n                    VStack(spacing: 20) {\n                        LogoSection()\n                        TrendingSection()\n                    }\n                    .padding()\n                }\n            }\n            .background(Color(\"SoftPink\")) // Change background to soft pink\n            \n            BottomSearchBar()\n        }\n        .edgesIgnoringSafeArea(.bottom)\n    }\n}\n\nstruct CustomNavigationBar: View {\n    var body: some View {\n        HStack {\n            Button(action: {}) {\n                Image(systemName: \"clock.arrow.circlepath\")\n            }\n            Button(action: {}) {\n                Image(systemName: \"heart.fill\") // Change to filled heart\n                    .foregroundColor(Color(\"Lavender\")) // Add lavender color\n            }\n            Button(action: {}) {\n                Image(systemName: \"slider.horizontal.3\")\n                    .overlay(Circle()\n                        .fill(Color(\"MintGreen\")) // Change to mint green\n                        .frame(width: 8, height: 8)\n                        .offset(x: 8, y: -8), alignment: .topTrailing)\n            }\n            Spacer()\n            Text(\"Chic\")\n                .font(.custom(\"Avenir-Medium\", size: 18)) // Change font\n            Text(\"Pro\")\n                .font(.custom(\"Avenir-Medium\", size: 18)) // Change font\n                .padding(.horizontal, 8)\n                .padding(.vertical, 4)\n                .background(Color(\"MintGreen\").opacity(0.2))\n                .cornerRadius(15) // Increase corner radius for softer look\n            Button(action: {}) {\n                Image(systemName: \"line.3.horizontal\")\n            }\n        }\n        .padding()\n        .foregroundColor(Color(\"DarkPurple\")) // Change text color to dark purple\n    }\n}\n\nstruct LogoSection: View {\n    var body: some View {\n        VStack(spacing: 10) {\n            Text(\"Encore\")\n                .font(.custom(\"Didot\", size: 40)) // Change to a more elegant font\n                .fontWeight(.bold)\n            Text(\"Discover Secondhand Treasures\")\n                .font(.custom(\"Avenir-Light\", size: 16))\n                .foregroundColor(Color(\"DarkPurple\"))\n        }\n    }\n}\n\nstruct TrendingItem: Identifiable {\n    let id = UUID()\n    let emoji: String\n    let description: String\n}\n\nstruct TrendingSection: View {\n    let trendingItems: [TrendingItem] = [\n        TrendingItem(emoji: \"👗\", description: \"Vintage Dresses\"),\n        TrendingItem(emoji: \"👜\", description: \"Designer Handbags\"),\n        TrendingItem(emoji: \"👠\", description: \"Statement Heels\"),\n        TrendingItem(emoji: \"💍\", description: \"Antique Jewelry\"),\n        TrendingItem(emoji: \"🧥\", description: \"Luxury Coats\")\n    ]\n    \n    var body: some View {\n        VStack(alignment: .leading, spacing: 10) {\n            HStack {\n                Text(\"Trending This Week\")\n                    .font(.custom(\"Avenir-Medium\", size: 18))\n                Image(systemName: \"sparkles\")\n                    .foregroundColor(Color(\"Lavender\"))\n            }\n            \n            ForEach(trendingItems) { item in\n                HStack {\n                    Text(item.emoji)\n                        .font(.system(size: 40))\n                        .frame(width: 50, height: 50)\n                        .background(Color(\"Lavender\").opacity(0.2))\n                        .cornerRadius(25) // Make it circular\n                    Text(item.description)\n                        .font(.custom(\"Avenir-Light\", size: 16))\n                        .lineLimit(1)\n                }\n            }\n        }\n    }\n}\n\nstruct BottomSearchBar: View {\n    @State private var searchText = \"\"\n    @State private var isSmartSearchEnabled = true\n    @State private var keyboardHeight: CGFloat = 0\n    \n    var body: some View {\n        GeometryReader { geometry in\n            VStack(spacing: 10) {\n                HStack {\n                    Text(\"Find Your Style ✨\")\n                        .font(.custom(\"Avenir-Medium\", size: 16))\n                    Spacer()\n                    Toggle(\"Smart Search\", isOn: $isSmartSearchEnabled)\n                }\n                .padding(.horizontal)\n                \n                HStack {\n                    Image(systemName: \"magnifyingglass\")\n                        .foregroundColor(Color(\"DarkPurple\"))\n                    TextField(\"Search for your next fashion find\", text: $searchText)\n                        .font(.custom(\"Avenir-Light\", size: 16))\n                        .textFieldStyle(PlainTextFieldStyle())\n                    Button(action: {}) {\n                        Image(systemName: \"arrow.right.circle.fill\")\n                            .foregroundColor(Color(\"MintGreen\"))\n                    }\n                }\n                .padding()\n                .background(Color(\"Lavender\").opacity(0.1))\n                .cornerRadius(20)\n                .padding(.horizontal)\n                .padding(.bottom, 10)\n            }\n            .padding(.top)\n            .background(Color.white)\n            .shadow(color: Color.black.opacity(0.1), radius: 5, x: 0, y: -5)\n            .offset(y: -self.keyboardHeight)\n            .animation(.easeOut(duration: 0.16))\n            .onAppear(perform: addKeyboardObserver)\n            .onDisappear(perform: removeKeyboardObserver)\n        }\n    }\n    \n    // ... (rest of the code remains the same)\n}\n\n#Preview {\n    ContentView()\n}\n"
    },
    {
      "text": "To complete this redesign, you'll need to add some custom colors to your asset catalog. Add the following colors:\n\n- SoftPink: A light, pastel pink (e.g., #FFE4E1)\n- Lavender: A soft purple (e.g., #E6E6FA)\n- MintGreen: A light, fresh green (e.g., #98FF98)\n- DarkPurple: A deep, rich purple for text (e.g., #4B0082)\n\nThese changes will give your app a more feminine and elegant look, appealing to a female audience. The softer color scheme, rounded shapes, and fashion-focused trending items should resonate well with your target users. The updated fonts (Didot for the logo, Avenir for other text) add a touch of sophistication and readability.\n\nRemember to test these changes with your target audience and gather feedback to further refine the design."
    }
  ]

  "#,
  TypeIR::class("DoCommandACReturnType"),
  {
    "sections": [
      {
        "code_language": "swift",
        "code": "import SwiftUI\n\nstruct ContentView: View {\n    var body: some View {\n        ZStack(alignment: .bottom) {\n            VStack(spacing: 0) {\n                CustomNavigationBar()\n                \n                ScrollView {\n                    VStack(spacing: 20) {\n                        LogoSection()\n                        TrendingSection()\n                    }\n                    .padding()\n                }\n            }\n            .background(Color(\"SoftPink\")) // Change background to soft pink\n            \n            BottomSearchBar()\n        }\n        .edgesIgnoringSafeArea(.bottom)\n    }\n}\n\nstruct CustomNavigationBar: View {\n    var body: some View {\n        HStack {\n            Button(action: {}) {\n                Image(systemName: \"clock.arrow.circlepath\")\n            }\n            Button(action: {}) {\n                Image(systemName: \"heart.fill\") // Change to filled heart\n                    .foregroundColor(Color(\"Lavender\")) // Add lavender color\n            }\n            Button(action: {}) {\n                Image(systemName: \"slider.horizontal.3\")\n                    .overlay(Circle()\n                        .fill(Color(\"MintGreen\")) // Change to mint green\n                        .frame(width: 8, height: 8)\n                        .offset(x: 8, y: -8), alignment: .topTrailing)\n            }\n            Spacer()\n            Text(\"Chic\")\n                .font(.custom(\"Avenir-Medium\", size: 18)) // Change font\n            Text(\"Pro\")\n                .font(.custom(\"Avenir-Medium\", size: 18)) // Change font\n                .padding(.horizontal, 8)\n                .padding(.vertical, 4)\n                .background(Color(\"MintGreen\").opacity(0.2))\n                .cornerRadius(15) // Increase corner radius for softer look\n            Button(action: {}) {\n                Image(systemName: \"line.3.horizontal\")\n            }\n        }\n        .padding()\n        .foregroundColor(Color(\"DarkPurple\")) // Change text color to dark purple\n    }\n}\n\nstruct LogoSection: View {\n    var body: some View {\n        VStack(spacing: 10) {\n            Text(\"Encore\")\n                .font(.custom(\"Didot\", size: 40)) // Change to a more elegant font\n                .fontWeight(.bold)\n            Text(\"Discover Secondhand Treasures\")\n                .font(.custom(\"Avenir-Light\", size: 16))\n                .foregroundColor(Color(\"DarkPurple\"))\n        }\n    }\n}\n\nstruct TrendingItem: Identifiable {\n    let id = UUID()\n    let emoji: String\n    let description: String\n}\n\nstruct TrendingSection: View {\n    let trendingItems: [TrendingItem] = [\n        TrendingItem(emoji: \"👗\", description: \"Vintage Dresses\"),\n        TrendingItem(emoji: \"👜\", description: \"Designer Handbags\"),\n        TrendingItem(emoji: \"👠\", description: \"Statement Heels\"),\n        TrendingItem(emoji: \"💍\", description: \"Antique Jewelry\"),\n        TrendingItem(emoji: \"🧥\", description: \"Luxury Coats\")\n    ]\n    \n    var body: some View {\n        VStack(alignment: .leading, spacing: 10) {\n            HStack {\n                Text(\"Trending This Week\")\n                    .font(.custom(\"Avenir-Medium\", size: 18))\n                Image(systemName: \"sparkles\")\n                    .foregroundColor(Color(\"Lavender\"))\n            }\n            \n            ForEach(trendingItems) { item in\n                HStack {\n                    Text(item.emoji)\n                        .font(.system(size: 40))\n                        .frame(width: 50, height: 50)\n                        .background(Color(\"Lavender\").opacity(0.2))\n                        .cornerRadius(25) // Make it circular\n                    Text(item.description)\n                        .font(.custom(\"Avenir-Light\", size: 16))\n                        .lineLimit(1)\n                }\n            }\n        }\n    }\n}\n\nstruct BottomSearchBar: View {\n    @State private var searchText = \"\"\n    @State private var isSmartSearchEnabled = true\n    @State private var keyboardHeight: CGFloat = 0\n    \n    var body: some View {\n        GeometryReader { geometry in\n            VStack(spacing: 10) {\n                HStack {\n                    Text(\"Find Your Style ✨\")\n                        .font(.custom(\"Avenir-Medium\", size: 16))\n                    Spacer()\n                    Toggle(\"Smart Search\", isOn: $isSmartSearchEnabled)\n                }\n                .padding(.horizontal)\n                \n                HStack {\n                    Image(systemName: \"magnifyingglass\")\n                        .foregroundColor(Color(\"DarkPurple\"))\n                    TextField(\"Search for your next fashion find\", text: $searchText)\n                        .font(.custom(\"Avenir-Light\", size: 16))\n                        .textFieldStyle(PlainTextFieldStyle())\n                    Button(action: {}) {\n                        Image(systemName: \"arrow.right.circle.fill\")\n                            .foregroundColor(Color(\"MintGreen\"))\n                    }\n                }\n                .padding()\n                .background(Color(\"Lavender\").opacity(0.1))\n                .cornerRadius(20)\n                .padding(.horizontal)\n                .padding(.bottom, 10)\n            }\n            .padding(.top)\n            .background(Color.white)\n            .shadow(color: Color.black.opacity(0.1), radius: 5, x: 0, y: -5)\n            .offset(y: -self.keyboardHeight)\n            .animation(.easeOut(duration: 0.16))\n            .onAppear(perform: addKeyboardObserver)\n            .onDisappear(perform: removeKeyboardObserver)\n        }\n    }\n    \n    // ... (rest of the code remains the same)\n}\n\n#Preview {\n    ContentView()\n}\n"
      },
      {
        "text": "To complete this redesign, you'll need to add some custom colors to your asset catalog. Add the following colors:\n\n- SoftPink: A light, pastel pink (e.g., #FFE4E1)\n- Lavender: A soft purple (e.g., #E6E6FA)\n- MintGreen: A light, fresh green (e.g., #98FF98)\n- DarkPurple: A deep, rich purple for text (e.g., #4B0082)\n\nThese changes will give your app a more feminine and elegant look, appealing to a female audience. The softer color scheme, rounded shapes, and fashion-focused trending items should resonate well with your target users. The updated fonts (Didot for the logo, Avenir for other text) add a touch of sophistication and readability.\n\nRemember to test these changes with your target audience and gather feedback to further refine the design."
      }
    ]
  }
);

const OBJECT_STREAM_TEST: &str = r#"
class Foo {
  a int
  c int
  b int
}

class Bar {
  foo Foo
  a int
}
"#;

test_partial_deserializer!(
  test_object_finished_ints,
  OBJECT_STREAM_TEST,
  r#"{"a": 1234,"b": 1234, "c": 1234}"#,
  TypeIR::class("Foo"),
  {"a": 1234, "b": 1234, "c": 1234}
);

test_deserializer!(
  test_empty_string_value,
  r#"
  class Foo {
    a string
  }
  "#,
  r#"{"a": ""}"#,
  TypeIR::class("Foo"),
  {"a": ""}
);

test_deserializer!(
  test_empty_string_value_1,
  r#"
  class Foo {
    a string
  }
  "#,
  r#"{a: ""}"#,
  TypeIR::class("Foo"),
  {"a": ""}
);

test_deserializer!(
  test_empty_string_value_2,
  r#"
  class Foo {
    a string
    b string
    res string[]
  }
  "#,
  r#"{
    a: "",
    b: "",
    res: []
  }"#,
  TypeIR::class("Foo"),
  {"a": "", "b": "", "res": []}
);

test_deserializer!(
  test_string_field_with_spaces,
  r#"
  class Foo {
    a string
    b string
    res string[]
  }
  "#,
  r#"{
    a: Hi friends!,
    b: hey world lets do something kinda cool
    so that we can test this out,
    res: [hello,
     world]
  }"#,
  TypeIR::class("Foo"),
  {
    "a": "Hi friends!",
    "b": "hey world lets do something kinda cool\n    so that we can test this out",
    "res": ["hello", "world"]
  }
);

test_deserializer!(
  test_recursive_type,
  r#"class Foo {
      pointer Foo?
  }"#,
  r#"
    The answer is
    {
      "pointer": {
        "pointer": null
      }
    },
  
    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "pointer": {
      "pointer": null,
    },
  }
);

test_deserializer!(
  test_recursive_type_missing_brackets_and_quotes,
  r#"class Foo {
      pointer Foo?
  }"#,
  r#"
    The answer is
    {
      "pointer": {
        pointer: null,
  
    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "pointer": {
      "pointer": null,
    },
  }
);

test_deserializer!(
  test_recursive_type_with_union,
  r#"class Foo {
      pointer Foo | int
  }"#,
  r#"
    The answer is
    {
      "pointer": {
        "pointer": 1,
      }
    },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "pointer": {
      "pointer": 1,
    },
  }
);

test_deserializer!(
  test_mutually_recursive_with_union,
  r#"class Foo {
      b Bar | int
  }
  
  class Bar {
    f Foo | int
  }
  "#,
  r#"
    The answer is
    {
      "b": {
        "f": {
          "b": 1
        },
      }
    },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "b": {
      "f": {
        "b": 1,
      },
    },
  }
);

test_deserializer!(
  test_recursive_type_with_union_missing_brackets_and_quotes,
  r#"class Foo {
      pointer Foo | int
  }"#,
  r#"
    The answer is
    {
      "pointer": {
        pointer: 1
    },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "pointer": {
      "pointer": 1,
    },
  }
);

test_deserializer!(
  test_recursive_union_on_multiple_fields_single_line,
  r#"class Foo {
      rec_one Foo | int
      rec_two Foo | int
  }
  "#,
  r#"
    The answer is
    {
      "rec_one": { "rec_one": 1, "rec_two": 2 },
      "rec_two": {
        "rec_one": { "rec_one": 1, "rec_two": 2 },
        "rec_two": { "rec_one": 1, "rec_two": 2 }
      }
    },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": {
      "rec_one": 1,
      "rec_two": 2
    },
    "rec_two": {
      "rec_one": {
        "rec_one": 1,
        "rec_two": 2
      },
      "rec_two": {
        "rec_one": 1,
        "rec_two": 2
      }
    },
  }
);

test_deserializer!(
  test_recursive_union_on_multiple_fields_single_line_without_quotes,
  r#"class Foo {
      rec_one Foo | int
      rec_two Foo | int
  }
  "#,
  r#"
    The answer is
    {
      rec_one: { rec_one: 1, rec_two: 2 },
      rec_two: {
        rec_one: { rec_one: 1, rec_two: 2 },
        rec_two: { rec_one: 1, rec_two: 2 }
      }
    },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": {
      "rec_one": 1,
      "rec_two": 2
    },
    "rec_two": {
      "rec_one": {
        "rec_one": 1,
        "rec_two": 2
      },
      "rec_two": {
        "rec_one": 1,
        "rec_two": 2
      }
    },
  }
);

test_deserializer!(
  test_recursive_single_line,
  r#"class Foo {
      rec_one Foo | int | bool
      rec_two Foo | int | bool
  }
  "#,
  r#"
    The answer is
    { rec_one: true, rec_two: false },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": true,
    "rec_two": false
  }
);

test_deserializer!(
  test_recursive_union_on_multiple_fields_single_line_without_quotes_complex,
  r#"class Foo {
      rec_one Foo | int | bool
      rec_two Foo | int | bool | null
  }
  "#,
  r#"
    The answer is
    {
      rec_one: { rec_one: { rec_one: true, rec_two: false }, rec_two: null },
      rec_two: {
        rec_one: { rec_one: { rec_one: 1, rec_two: 2 }, rec_two: null },
        rec_two: { rec_one: 1, rec_two: null }
      }
    },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": {
      "rec_one": {
        "rec_one": true,
        "rec_two": false
      },
      "rec_two": null
    },
    "rec_two": {
      "rec_one": {
        "rec_one": {
          "rec_one": 1,
          "rec_two": 2
        },
        "rec_two": null
      },
      "rec_two": {
        "rec_one": 1,
        "rec_two": null
      }
    },
  }
);

const OPTIONAL_LIST_AND_MAP: &str = r#"
class OptionalListAndMap {
  p string[]?
  q map<string, string>?
}
"#;

test_partial_deserializer_streaming!(
  test_optional_list,
  OPTIONAL_LIST_AND_MAP,
  r#"
            ```json
            {
              "p": ["test"],
              "q": {
                "test": "ok"
              }
            }
            ```
  "#,
  TypeIR::class("OptionalListAndMap"),
  {"p": ["test"], "q": { "test": "ok" }}
);

const INTEG_TEST_FAILURE_STR: &str = r#"
[
  {
    "prop1": "In the realm of artificial intelligence, advancements have been remarkable. Between neural networks and cutting-edge algorithms, the landscape of machine learning has evolved dramatically. From the development of self-driving cars to sophisticated chatbots that can engage in human-like conversations, AI technology has become an integral aspect of modern life. Researchers are continually pushing the boundaries of what is possible, exploring deep learning techniques that enable machines to learn from extensive datasets. The application of AI spans various industries including healthcare, where predictive analytics aids in diagnostics, to finance, where algorithms manage investment portfolios. As AI continues to adapt and grow, ethical considerations surrounding data privacy and decision-making processes become increasingly important. Ongoing debates question the implications of relying on AI and machine learning for critical functions in society. Moreover, governments and organizations alike are grappling with the challenges of regulation and oversight in this fast-paced field. The future of AI seems bright, but it also poses inquiries into trust, accountability, and the long-term effects on the job market. As we look ahead, the collaboration between humans and machines could redefine productivity and creativity, paving the way for innovative solutions to complex problems that society faces.",
    "prop2": 1
  }
]
"#;

const INTEG_TEST_FAILURE_SCHEMA: &str = r#"
class TestOutputClass {
  prop1 string @description("A long string with about 200 words")
  prop2 int
}
"#;

test_partial_deserializer_streaming!(
    test_integ_test_failure,
    INTEG_TEST_FAILURE_SCHEMA,
    INTEG_TEST_FAILURE_STR,
    TypeIR::class("TestOutputClass"),
    { "prop1": "In the realm of artificial intelligence, advancements have been remarkable. Between neural networks and cutting-edge algorithms, the landscape of machine learning has evolved dramatically. From the development of self-driving cars to sophisticated chatbots that can engage in human-like conversations, AI technology has become an integral aspect of modern life. Researchers are continually pushing the boundaries of what is possible, exploring deep learning techniques that enable machines to learn from extensive datasets. The application of AI spans various industries including healthcare, where predictive analytics aids in diagnostics, to finance, where algorithms manage investment portfolios. As AI continues to adapt and grow, ethical considerations surrounding data privacy and decision-making processes become increasingly important. Ongoing debates question the implications of relying on AI and machine learning for critical functions in society. Moreover, governments and organizations alike are grappling with the challenges of regulation and oversight in this fast-paced field. The future of AI seems bright, but it also poses inquiries into trust, accountability, and the long-term effects on the job market. As we look ahead, the collaboration between humans and machines could redefine productivity and creativity, paving the way for innovative solutions to complex problems that society faces.",
      "prop2": 1
    }
);

test_deserializer!(
  test_string_in_object_with_unescaped_quotes,
  r#"class Foo {
      rec_one string
      rec_two string
      also_rec_one string
  }
  "#,
  r#"
    The answer is
    { rec_one: "and then i said \"hi\", and also \"bye\"", rec_two: "and then i said "hi", and also "bye"", "also_rec_one": ok },

    Anything else I can help with?
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": "and then i said \"hi\", and also \"bye\"",
    "rec_two": "and then i said \"hi\", and also \"bye\"",
    "also_rec_one": "ok"
  }
);

test_partial_deserializer_streaming!(
  test_string_in_object_with_unescaped_quotes_2,
  r#"class Foo {
      rec_one string
      rec_two string
  }
  "#,
  r#"
    The answer is
    { rec_one: "and then i said \"hi\"
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": "and then i said \"hi\"\n  ",
    "rec_two": null
  }
);

test_partial_deserializer_streaming!(
  test_string_in_object_with_unescaped_quotes_3,
  r#"class Foo {
      rec_one string
      rec_two string
  }
  "#,
  r#"
    The answer is
    { rec_one: "and then i said "hi", and also "bye""
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": "and then i said \"hi\", and also \"bye\"",
    "rec_two": null
  }
);

test_deserializer!(
  test_array_in_object,
  r#"class Foo {
      rec_one string[]
      rec_two string[]
  }
  "#,
  r#"
    The answer is
    { rec_one: ["first with "quotes", and also "more"", "second"], rec_two: ["third", "fourth"] },
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": vec!["first with \"quotes\", and also \"more\"", "second"],
    "rec_two": vec!["third", "fourth"]
  }
);

test_partial_deserializer_streaming!(
  test_partial_array_in_object,
  r#"class Foo {
      rec_one string[]
      rec_two string[]
  }
  "#,
  r#"
    The answer is
    { rec_one: ["first", "second"
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": vec!["first", "second"],
    "rec_two": []
  }
);

test_partial_deserializer_streaming!(
  test_array_with_unescaped_quotes,
  r#"class Foo {
      rec_one string[]
      rec_two string[]
  }
  "#,
  r#"
    The answer is
    { rec_one: ["and then i said "hi", "and also "bye"]
  "#,
  TypeIR::class("Foo"),
  {
    "rec_one": vec!["and then i said \"hi\", \"and also \"bye"],
    "rec_two": []
  }
);

test_deserializer!(
  test_enum_without_leading_newline,
  r#"enum Foo {
    FOO
    BAR
  }

  class WithFoo {
    foo Foo
    name string
  }
  "#,
  r#"
    {foo:FOO, name: "Greg"}
  "#,
  TypeIR::class("WithFoo"),
  {
    "foo": "FOO",
    "name": "Greg"
  }
);

test_deserializer!(
  test_aliases_with_capitalized_key,
  CLASS_WITH_ALIASES,
  // Key21 is now capitalized, but we should still be able to parse it.
  r#"{
      "key-dash": "This is a value with a dash",
      "Key21": "This is a value for key21",
      "key with space": "This is a value with space",
      "key4": "This is a value for key4",
      "key.with.punctuation/123": "This is a value with punctuation and numbers"
    }"#,
  TypeIR::class("TestClassAlias"),
  {
      "key": "This is a value with a dash",
      "key2": "This is a value for key21",
      "key3": "This is a value with space",
      "key4": "This is a value for key4",
      "key5": "This is a value with punctuation and numbers"
  }
);

test_deserializer!(
  test_class_with_capitalization,
  CLASS_SIMPLE,
  r#"{"Answer": {" content ": 78.54}}"#,
  TypeIR::class("SimpleTest"),
  {
      "answer": {
          "content": 78.54
      }
  }
);
