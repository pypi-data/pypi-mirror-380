use serde_json;
use std::fmt::{Debug, Display, Formatter};

#[derive(Debug)]
pub enum RPCError {
    StatusCheckFailed(String),
    DeserializationFailed(serde_json::Error),
    ConnectionFailed,
}

impl Display for RPCError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            RPCError::StatusCheckFailed(message) => {
                write!(f, "Command returned with error status: {message}")
            }
            RPCError::DeserializationFailed(error) => {
                write!(f, "Failed to deserialize result: {error}")
            }
            RPCError::ConnectionFailed => {
                write!(f, "Failed to connect to RPC API")
            }
        }
    }
}

impl std::error::Error for RPCError {}

impl From<serde_json::Error> for RPCError {
    fn from(value: serde_json::Error) -> Self {
        Self::DeserializationFailed(value)
    }
}
impl From<std::io::Error> for RPCError {
    fn from(_: std::io::Error) -> Self {
        Self::ConnectionFailed
    }
}
