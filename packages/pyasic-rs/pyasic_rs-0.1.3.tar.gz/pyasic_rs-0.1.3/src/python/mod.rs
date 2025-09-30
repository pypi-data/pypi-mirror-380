use pyo3::prelude::*;

mod data;
mod factory;
mod miner;

#[pymodule(module = "asic_rs")]
mod asic_rs {
    #[pymodule_export]
    use super::factory::MinerFactory;
    #[pymodule_export]
    use super::miner::Miner;

    #[pymodule_export]
    use super::data::HashAlgorithm;
    #[pymodule_export]
    use super::data::MinerFirmware;
    #[pymodule_export]
    use super::data::MinerMake;
    #[pymodule_export]
    use super::data::MinerModel;
}
