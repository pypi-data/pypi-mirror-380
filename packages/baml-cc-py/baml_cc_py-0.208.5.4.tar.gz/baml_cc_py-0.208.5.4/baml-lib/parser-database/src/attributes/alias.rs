use internal_baml_diagnostics::DatamodelError;

use crate::{coerce, context::Context, types::Attributes};

pub(super) fn visit_alias_attribute(attributes: &mut Attributes, ctx: &mut Context<'_>) {
    match ctx.visit_default_arg_with_idx("alias") {
        Ok((_, name)) => {
            if attributes.alias().is_some() {
                ctx.push_attribute_validation_error("cannot be specified more than once", false);
            } else if let Some(result) = name.to_unresolved_value(ctx.diagnostics) {
                if result.as_str().is_some() {
                    attributes.add_alias(result);
                } else {
                    ctx.push_error(DatamodelError::new_validation_error(
                        "must be a string.",
                        result.meta().clone(),
                    ));
                }
            }
        }
        Err(err) => ctx.push_error(err), // not flattened for error handing legacy reasons
    };
}
