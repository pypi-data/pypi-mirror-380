use std::fmt::Display;

use super::{Span, WithName, WithSpan};

/// An identifier the refers to a field or type in a different location.
#[derive(Debug, Clone, PartialEq)]
pub struct RefIdentifier {
    pub path: Vec<String>,
    /// The identifier contents.
    pub name: String,
    pub full_name: String,
}

#[derive(Debug, Clone, PartialEq)]
pub enum Identifier {
    /// Starts with env.*
    ENV(String, Span),
    /// The path to a Local Identifer + the local identifer. Separated by '.'
    Ref(RefIdentifier, Span),
    /// A string without spaces or '.' Always starts with a letter. May contain numbers
    Local(String, Span),
    /// A string without spaces, but contains '-'
    String(String, Span),
    /// Something that cannot be used for anything.
    Invalid(String, Span),
}

impl Identifier {
    pub fn is_valid_type(&self) -> bool {
        match self {
            Identifier::ENV(_, _) => false,
            Identifier::Ref(_, _) => true,
            Identifier::Local(_, _) => true,
            Identifier::String(_, _) => false,
            Identifier::Invalid(_, _) => false,
        }
    }

    pub fn is_valid_type_name(&self) -> bool {
        match self {
            Identifier::ENV(_, _) => false,
            Identifier::Ref(_, _) => true,
            Identifier::Local(_, _) => true,

            Identifier::String(_, _) => false,
            Identifier::Invalid(_, _) => false,
        }
    }

    pub fn is_valid_value(&self) -> bool {
        match self {
            Identifier::ENV(_, _) => true,
            Identifier::Local(_, _) => true,
            Identifier::String(_, _) => true,
            Identifier::Ref(_, _) => false,

            Identifier::Invalid(_, _) => false,
        }
    }

    pub fn assert_eq_up_to_span(&self, other: &Identifier) {
        use Identifier::*;
        match (self, other) {
            (ENV(e1, _), ENV(e2, _)) => assert_eq!(e1, e2),
            (ENV(_, _), _) => panic!("Mismatched identifiers: {self:?}, {other:?}"),
            (Local(l1, _), Local(l2, _)) => assert_eq!(l1, l2),
            (Local(_, _), _) => panic!("Mismatched identifiers: {self:?}, {other:?}"),
            (Ref(r1, _), Ref(r2, _)) => assert_eq!(r1, r2),
            (Ref(_, _), _) => panic!("Mismatched identifiers: {self:?}, {other:?}"),
            (Identifier::String(s1, _), Identifier::String(s2, _)) => assert_eq!(s1, s2),
            (Identifier::String(_, _), _) => panic!("Mismatched identifiers: {self:?}, {other:?}"),
            (Invalid(i1, _), Invalid(i2, _)) => assert_eq!(i1, i2),
            (Invalid(_, _), _) => panic!("Mismatched identifiers: {self:?}, {other:?}"),
        }
    }
}

impl WithSpan for Identifier {
    fn span(&self) -> &Span {
        match self {
            Identifier::ENV(_, span) => span,
            Identifier::Ref(_, span) => span,
            Identifier::Local(_, span) => span,

            Identifier::String(_, span) => span,
            Identifier::Invalid(_, span) => span,
        }
    }
}

impl WithName for Identifier {
    fn name(&self) -> &str {
        match self {
            Identifier::Ref(ref_identifier, _) => &ref_identifier.full_name,
            Identifier::Local(name, _) => name,
            Identifier::String(s, _) => s,
            Identifier::ENV(name, _) => name,
            Identifier::Invalid(name, _) => name,
        }
    }
}

impl From<(&str, Span)> for Identifier {
    fn from((s, span): (&str, Span)) -> Self {
        match s {
            s if s.starts_with("env.") => Identifier::ENV(s[4..].to_string(), span),
            s if s.contains('.') => Identifier::Ref(
                RefIdentifier {
                    path: s.split('.').map(String::from).collect::<Vec<_>>()
                        [..s.split('.').count() - 1]
                        .to_vec(),
                    name: s.split('.').next_back().unwrap().to_string(),
                    full_name: s.to_string(),
                },
                span,
            ),
            "env" => Identifier::Invalid("env".into(), span),
            other if other.contains('-') => Identifier::String(other.to_string(), span),
            other => Identifier::Local(other.to_string(), span),
        }
    }
}

impl Display for Identifier {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Identifier::ENV(s, _) => write!(f, "env.{s}"),
            Identifier::Ref(ref_identifier, _) => f.write_str(&ref_identifier.full_name),
            Identifier::Local(s, _) => f.write_str(s),
            Identifier::String(s, _) => f.write_str(s),
            Identifier::Invalid(s, _) => f.write_str(s),
        }
    }
}
