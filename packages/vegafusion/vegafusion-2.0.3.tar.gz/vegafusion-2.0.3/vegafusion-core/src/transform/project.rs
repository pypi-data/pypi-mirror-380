use crate::error::Result;
use crate::proto::gen::transforms::Project;
use crate::spec::transform::project::ProjectTransformSpec;
use crate::transform::TransformDependencies;

use crate::task_graph::task::InputVariable;

impl Project {
    pub fn try_new(spec: &ProjectTransformSpec) -> Result<Self> {
        Ok(Self {
            fields: spec.fields.clone(),
        })
    }
}

impl TransformDependencies for Project {
    fn input_vars(&self) -> Vec<InputVariable> {
        Default::default()
    }
}
