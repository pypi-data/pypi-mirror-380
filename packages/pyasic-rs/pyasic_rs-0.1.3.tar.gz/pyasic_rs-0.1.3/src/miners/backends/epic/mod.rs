use semver;
use std::net::IpAddr;

pub use v1::PowerPlayV1;

use crate::data::device::MinerModel;
use crate::miners::backends::traits::*;

pub mod v1;

pub struct PowerPlay;

impl MinerConstructor for PowerPlay {
    #[allow(clippy::new_ret_no_self)]
    fn new(ip: IpAddr, model: MinerModel, _: Option<semver::Version>) -> Box<dyn Miner> {
        Box::new(PowerPlayV1::new(ip, model))
    }
}
