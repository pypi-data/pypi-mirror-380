use crate::proto::gen::transforms::{AggregateOp, JoinAggregate};
use crate::spec::transform::aggregate::AggregateOpSpec;
use crate::spec::transform::joinaggregate::JoinAggregateTransformSpec;
use crate::transform::TransformDependencies;
use itertools::Itertools;

impl JoinAggregate {
    pub fn new(transform: &JoinAggregateTransformSpec) -> Self {
        let fields: Vec<_> = transform
            .fields
            .iter()
            .map(|f| f.as_ref().map(|f| f.field()).unwrap_or_default())
            .collect();

        let groupby: Vec<_> = transform
            .groupby
            .as_ref()
            .map(|groupby| groupby.iter().map(|f| f.field()).unique().collect())
            .unwrap_or_default();

        // Initialize aliases with those potentially provided in field objects
        // (e.g. {"field": "foo", "as": "bar"}
        let mut aliases: Vec<_> = transform
            .fields
            .iter()
            .map(|f| f.as_ref().and_then(|f| f.as_()).unwrap_or_default())
            .collect();

        // Overwrite aliases with those provided in the as_ prop of the transform
        for (i, as_) in transform.as_.clone().unwrap_or_default().iter().enumerate() {
            if as_.is_some() {
                aliases[i] = as_.clone().unwrap();
            }
        }

        let ops: Vec<_> = transform
            .ops
            .iter()
            .map(|op| match op {
                AggregateOpSpec::Count => AggregateOp::Count as i32,
                AggregateOpSpec::Valid => AggregateOp::Valid as i32,
                AggregateOpSpec::Missing => AggregateOp::Missing as i32,
                AggregateOpSpec::Distinct => AggregateOp::Distinct as i32,
                AggregateOpSpec::Sum => AggregateOp::Sum as i32,
                AggregateOpSpec::Product => AggregateOp::Product as i32,
                AggregateOpSpec::Mean => AggregateOp::Mean as i32,
                AggregateOpSpec::Average => AggregateOp::Average as i32,
                AggregateOpSpec::Variance => AggregateOp::Variance as i32,
                AggregateOpSpec::Variancep => AggregateOp::Variancep as i32,
                AggregateOpSpec::Stdev => AggregateOp::Stdev as i32,
                AggregateOpSpec::Stdevp => AggregateOp::Stdevp as i32,
                AggregateOpSpec::Stderr => AggregateOp::Stderr as i32,
                AggregateOpSpec::Median => AggregateOp::Median as i32,
                AggregateOpSpec::Q1 => AggregateOp::Q1 as i32,
                AggregateOpSpec::Q3 => AggregateOp::Q3 as i32,
                AggregateOpSpec::Ci0 => AggregateOp::Ci0 as i32,
                AggregateOpSpec::Ci1 => AggregateOp::Ci1 as i32,
                AggregateOpSpec::Min => AggregateOp::Min as i32,
                AggregateOpSpec::Max => AggregateOp::Max as i32,
                AggregateOpSpec::Argmin => AggregateOp::Argmin as i32,
                AggregateOpSpec::Argmax => AggregateOp::Argmax as i32,
                AggregateOpSpec::Values => AggregateOp::Values as i32,
            })
            .collect();

        Self {
            groupby,
            fields,
            ops,
            aliases,
        }
    }
}

pub fn op_name(op: AggregateOp) -> String {
    match op {
        AggregateOp::Count => "count",
        AggregateOp::Valid => "valid",
        AggregateOp::Missing => "missing",
        AggregateOp::Distinct => "distinct",
        AggregateOp::Sum => "sum",
        AggregateOp::Product => "product",
        AggregateOp::Mean => "mean",
        AggregateOp::Average => "average",
        AggregateOp::Variance => "variance",
        AggregateOp::Variancep => "variancep",
        AggregateOp::Stdev => "stdev",
        AggregateOp::Stdevp => "stdevp",
        AggregateOp::Stderr => "stderr",
        AggregateOp::Median => "median",
        AggregateOp::Q1 => "q1",
        AggregateOp::Q3 => "q3",
        AggregateOp::Ci0 => "ci0",
        AggregateOp::Ci1 => "ci1",
        AggregateOp::Min => "min",
        AggregateOp::Max => "max",
        AggregateOp::Argmin => "argmin",
        AggregateOp::Argmax => "argmax",
        AggregateOp::Values => "values",
    }
    .to_string()
}

impl TransformDependencies for JoinAggregate {}
