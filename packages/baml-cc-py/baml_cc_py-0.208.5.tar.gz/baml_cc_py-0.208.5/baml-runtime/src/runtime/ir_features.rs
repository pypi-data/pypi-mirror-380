use internal_baml_core::ir::{FunctionWalker, TestCaseWalker};

use super::InternalBamlRuntime;
use crate::{
    internal::ir_features::{IrFeatures, WithInternal},
    InternalRuntimeInterface,
};

impl WithInternal for InternalBamlRuntime {
    fn features(&self) -> IrFeatures {
        let ir = self.ir();

        IrFeatures::from(vec![], ir.walk_functions().any(|f| f.is_v2()), vec![])
    }

    fn walk_functions(&self) -> impl ExactSizeIterator<Item = FunctionWalker<'_>> {
        self.ir().walk_functions()
    }

    fn walk_tests(&self) -> impl Iterator<Item = TestCaseWalker<'_>> {
        self.ir().walk_function_test_pairs()
    }
}
