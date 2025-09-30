use serde::{Deserialize, Serialize};
use serde_json::Value;
use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct AxisSpec {
    pub scale: String,

    #[serde(rename = "formatType", skip_serializing_if = "Option::is_none")]
    pub format_type: Option<AxisFormatTypeSpec>,

    #[serde(flatten)]
    pub extra: HashMap<String, Value>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum AxisFormatTypeSpec {
    Number,
    Time,
    Utc,
}
