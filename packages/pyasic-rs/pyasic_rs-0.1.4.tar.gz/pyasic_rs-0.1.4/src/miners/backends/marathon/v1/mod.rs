use crate::data::board::{BoardData, ChipData};
use crate::data::device::{DeviceInfo, HashAlgorithm, MinerFirmware, MinerModel};
use crate::data::device::{MinerControlBoard, MinerMake};
use crate::data::fan::FanData;
use crate::data::hashrate::{HashRate, HashRateUnit};
use crate::data::pool::{PoolData, PoolURL};
use crate::miners::backends::traits::*;
use crate::miners::commands::MinerCommand;
use crate::miners::data::{
    DataCollector, DataExtensions, DataExtractor, DataField, DataLocation, get_by_pointer,
};
use anyhow::{Result, anyhow, bail};
use async_trait::async_trait;
use macaddr::MacAddr;
use measurements::{AngularVelocity, Frequency, Power, Temperature, Voltage};
use serde_json::Value;
use std::collections::HashMap;
use std::net::IpAddr;
use std::str::FromStr;
use std::time::Duration;

use crate::data::message::{MessageSeverity, MinerMessage};
use web::MaraWebAPI;

mod web;

#[derive(Debug)]
pub struct MaraV1 {
    ip: IpAddr,
    web: MaraWebAPI,
    device_info: DeviceInfo,
}

impl MaraV1 {
    pub fn new(ip: IpAddr, model: MinerModel) -> Self {
        MaraV1 {
            ip,
            web: MaraWebAPI::new(ip, 80),
            device_info: DeviceInfo::new(
                MinerMake::from(model),
                model,
                MinerFirmware::Marathon,
                HashAlgorithm::SHA256,
            ),
        }
    }
}

#[async_trait]
impl APIClient for MaraV1 {
    async fn get_api_result(&self, command: &MinerCommand) -> Result<Value> {
        match command {
            MinerCommand::WebAPI { .. } => self.web.get_api_result(command).await,
            _ => Err(anyhow!("Unsupported command type for Marathon API")),
        }
    }
}

impl GetDataLocations for MaraV1 {
    fn get_locations(&self, data_field: DataField) -> Vec<DataLocation> {
        fn cmd(endpoint: &'static str) -> MinerCommand {
            MinerCommand::WebAPI {
                command: endpoint,
                parameters: None,
            }
        }

        let brief_cmd = cmd("brief");
        let overview_cmd = cmd("overview");
        let hashboards_cmd = cmd("hashboards");
        let fans_cmd = cmd("fans");
        let pools_cmd = cmd("pools");
        let network_config_cmd = cmd("network_config");
        let miner_config_cmd = cmd("miner_config");
        let locate_miner_cmd = cmd("locate_miner");
        let details_cmd = cmd("details");
        let messages_cmd = cmd("event_chart");

        match data_field {
            DataField::Mac => vec![(
                overview_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/mac"),
                    tag: None,
                },
            )],
            DataField::FirmwareVersion => vec![(
                overview_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/version_firmware"),
                    tag: None,
                },
            )],
            DataField::ControlBoardVersion => vec![(
                overview_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/control_board"),
                    tag: None,
                },
            )],
            DataField::Hostname => vec![(
                network_config_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/hostname"),
                    tag: None,
                },
            )],
            DataField::Hashrate => vec![(
                brief_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/hashrate_realtime"),
                    tag: None,
                },
            )],
            DataField::ExpectedHashrate => vec![(
                brief_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/hashrate_ideal"),
                    tag: None,
                },
            )],
            DataField::Hashboards => vec![
                (
                    details_cmd,
                    DataExtractor {
                        func: get_by_pointer,
                        key: Some("/hashboard_infos"),
                        tag: Some("chip_data"),
                    },
                ),
                (
                    hashboards_cmd,
                    DataExtractor {
                        func: get_by_pointer,
                        key: Some("/hashboards"),
                        tag: Some("hb_temps"),
                    },
                ),
            ],
            DataField::Wattage => vec![(
                brief_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/power_consumption_estimated"),
                    tag: None,
                },
            )],
            DataField::WattageLimit => vec![(
                miner_config_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/mode/concorde/power-target"),
                    tag: None,
                },
            )],
            DataField::Fans => vec![(
                fans_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/fans"),
                    tag: None,
                },
            )],
            DataField::LightFlashing => vec![(
                locate_miner_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/blinking"),
                    tag: None,
                },
            )],
            DataField::IsMining => vec![(
                brief_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/status"),
                    tag: None,
                },
            )],
            DataField::Uptime => vec![(
                brief_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/elapsed"),
                    tag: None,
                },
            )],
            DataField::Pools => vec![(
                pools_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some(""),
                    tag: None,
                },
            )],
            DataField::Messages => vec![(
                messages_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/event_flags"),
                    tag: None,
                },
            )],
            _ => vec![],
        }
    }
}

impl GetIP for MaraV1 {
    fn get_ip(&self) -> IpAddr {
        self.ip
    }
}

impl GetDeviceInfo for MaraV1 {
    fn get_device_info(&self) -> DeviceInfo {
        self.device_info
    }
}

impl CollectData for MaraV1 {
    fn get_collector(&self) -> DataCollector<'_> {
        DataCollector::new(self)
    }
}

impl GetMAC for MaraV1 {
    fn parse_mac(&self, data: &HashMap<DataField, Value>) -> Option<MacAddr> {
        data.extract::<String>(DataField::Mac)
            .and_then(|mac_str| MacAddr::from_str(&mac_str.to_uppercase()).ok())
    }
}

impl GetSerialNumber for MaraV1 {}

impl GetHostname for MaraV1 {
    fn parse_hostname(&self, data: &HashMap<DataField, Value>) -> Option<String> {
        data.extract::<String>(DataField::Hostname)
    }
}

impl GetApiVersion for MaraV1 {}

impl GetFirmwareVersion for MaraV1 {
    fn parse_firmware_version(&self, data: &HashMap<DataField, Value>) -> Option<String> {
        data.extract::<String>(DataField::FirmwareVersion)
    }
}

impl GetControlBoardVersion for MaraV1 {
    fn parse_control_board_version(
        &self,
        data: &HashMap<DataField, Value>,
    ) -> Option<MinerControlBoard> {
        let cb = data.extract::<String>(DataField::ControlBoardVersion)?;
        if cb.starts_with("MaraCB") {
            // Ignore version (eg `MaraCB_v1.4`)
            return Some(MinerControlBoard::MaraCB);
        };
        MinerControlBoard::from_str(cb.as_str()).ok()
    }
}

impl MaraV1 {
    fn parse_chip_data(asic_infos: &Value) -> Vec<ChipData> {
        asic_infos
            .as_array()
            .map(|chips| {
                chips
                    .iter()
                    .filter_map(|chip| {
                        let position = chip.get("index")?.as_u64()? as u16;

                        let hashrate =
                            chip.get("hashrate_avg")
                                .and_then(|hr| hr.as_f64())
                                .map(|value| HashRate {
                                    value,
                                    unit: HashRateUnit::GigaHash,
                                    algo: "SHA256".to_string(),
                                });

                        let voltage = chip
                            .get("voltage")
                            .and_then(|v| v.as_f64())
                            .map(Voltage::from_volts);

                        let frequency = chip
                            .get("frequency")
                            .and_then(|f| f.as_f64())
                            .map(Frequency::from_megahertz);

                        let working = chip
                            .get("hashrate_avg")
                            .and_then(|hr| hr.as_f64())
                            .map(|hr| hr > 0.0);

                        Some(ChipData {
                            position,
                            hashrate,
                            temperature: None,
                            voltage,
                            frequency,
                            tuned: None,
                            working,
                        })
                    })
                    .collect()
            })
            .unwrap_or_default()
    }
}

impl GetHashboards for MaraV1 {
    fn parse_hashboards(&self, data: &HashMap<DataField, Value>) -> Vec<BoardData> {
        let mut hashboards: Vec<BoardData> = Vec::new();

        if let Some(expected_boards) = self.device_info.hardware.boards {
            for i in 0..expected_boards {
                hashboards.push(BoardData {
                    position: i,
                    hashrate: None,
                    expected_hashrate: None,
                    board_temperature: None,
                    intake_temperature: None,
                    outlet_temperature: None,
                    expected_chips: self.device_info.hardware.chips,
                    working_chips: None,
                    serial_number: None,
                    chips: vec![],
                    voltage: None,
                    frequency: None,
                    tuned: None,
                    active: None,
                });
            }
        }

        if let Some(hashboards_data) = data
            .get(&DataField::Hashboards)
            .and_then(|v| v.pointer("/chip_data"))
            && let Some(hb_array) = hashboards_data.as_array()
        {
            let hashboard_temps = data
                .get(&DataField::Hashboards)
                .and_then(|v| v.pointer("/hb_temps"))
                .and_then(|v| v.as_array());

            for hb in hb_array {
                if let Some(idx) = hb.get("index").and_then(|v| v.as_u64())
                    && let Some(hashboard) = hashboards.get_mut(idx as usize)
                {
                    hashboard.position = idx as u8;

                    let hb_temps = hashboard_temps
                        .and_then(|temps| temps.get(idx as usize))
                        .and_then(|v| v.as_object());

                    if let Some(hashrate) = hb.get("hashrate_avg").and_then(|v| v.as_f64()) {
                        hashboard.hashrate = Some(HashRate {
                            value: hashrate,
                            unit: HashRateUnit::GigaHash,
                            algo: String::from("SHA256"),
                        });
                    }

                    if let Some(temps_obj) = hb_temps {
                        if let Some(temp_pcb) =
                            temps_obj.get("temperature_pcb").and_then(|v| v.as_array())
                        {
                            let temps: Vec<f64> =
                                temp_pcb.iter().filter_map(|t| t.as_f64()).collect();
                            if !temps.is_empty() {
                                let avg_temp = temps.iter().sum::<f64>() / temps.len() as f64;
                                hashboard.board_temperature =
                                    Some(Temperature::from_celsius(avg_temp));
                            }
                        }

                        if let Some(temp_raw) =
                            temps_obj.get("temperature_raw").and_then(|v| v.as_array())
                        {
                            let temps: Vec<f64> =
                                temp_raw.iter().filter_map(|t| t.as_f64()).collect();
                            if !temps.is_empty() {
                                let avg_temp = temps.iter().sum::<f64>() / temps.len() as f64;
                                hashboard.intake_temperature =
                                    Some(Temperature::from_celsius(avg_temp));
                            }
                        }
                    }

                    if let Some(asic_num) = hb.get("asic_num").and_then(|v| v.as_u64()) {
                        hashboard.working_chips = Some(asic_num as u16);
                    }

                    if let Some(serial) = hb.get("serial_number").and_then(|v| v.as_str()) {
                        hashboard.serial_number = Some(serial.to_string());
                    }

                    if let Some(voltage) = hb.get("voltage").and_then(|v| v.as_f64()) {
                        hashboard.voltage = Some(Voltage::from_volts(voltage));
                    }

                    if let Some(frequency) = hb.get("frequency_avg").and_then(|v| v.as_f64()) {
                        hashboard.frequency = Some(Frequency::from_megahertz(frequency));
                    }

                    if let Some(expected_hashrate) =
                        hb.get("hashrate_ideal").and_then(|v| v.as_f64())
                    {
                        hashboard.expected_hashrate = Some(HashRate {
                            value: expected_hashrate,
                            unit: HashRateUnit::GigaHash,
                            algo: String::from("SHA256"),
                        });
                    }

                    hashboard.active = Some(true);

                    if let Some(asic_infos) = hb.get("asic_infos") {
                        hashboard.chips = Self::parse_chip_data(asic_infos);
                    }
                }
            }
        }

        hashboards
    }
}

impl GetHashrate for MaraV1 {
    fn parse_hashrate(&self, data: &HashMap<DataField, Value>) -> Option<HashRate> {
        data.extract::<f64>(DataField::Hashrate)
            .map(|rate| HashRate {
                value: rate,
                unit: HashRateUnit::TeraHash,
                algo: String::from("SHA256"),
            })
    }
}

impl GetExpectedHashrate for MaraV1 {
    fn parse_expected_hashrate(&self, data: &HashMap<DataField, Value>) -> Option<HashRate> {
        data.extract::<f64>(DataField::ExpectedHashrate)
            .map(|rate| HashRate {
                value: rate,
                unit: HashRateUnit::GigaHash,
                algo: String::from("SHA256"),
            })
    }
}

impl GetFans for MaraV1 {
    fn parse_fans(&self, data: &HashMap<DataField, Value>) -> Vec<FanData> {
        let mut fans: Vec<FanData> = Vec::new();

        if let Some(fans_data) = data.get(&DataField::Fans)
            && let Some(fans_array) = fans_data.as_array()
        {
            for (i, fan) in fans_array.iter().enumerate() {
                if let Some(speed) = fan.get("current_speed").and_then(|v| v.as_f64()) {
                    fans.push(FanData {
                        position: i as i16,
                        rpm: Some(AngularVelocity::from_rpm(speed)),
                    });
                }
            }
        }

        if fans.is_empty()
            && let Some(expected_fans) = self.device_info.hardware.fans
        {
            for i in 0..expected_fans {
                fans.push(FanData {
                    position: i as i16,
                    rpm: None,
                });
            }
        }

        fans
    }
}

impl GetPsuFans for MaraV1 {}

impl GetFluidTemperature for MaraV1 {}

impl GetWattage for MaraV1 {
    fn parse_wattage(&self, data: &HashMap<DataField, Value>) -> Option<Power> {
        data.extract::<f64>(DataField::Wattage)
            .map(Power::from_watts)
    }
}

impl GetWattageLimit for MaraV1 {
    fn parse_wattage_limit(&self, data: &HashMap<DataField, Value>) -> Option<Power> {
        data.extract::<f64>(DataField::WattageLimit)
            .map(Power::from_watts)
    }
}

impl GetLightFlashing for MaraV1 {
    fn parse_light_flashing(&self, data: &HashMap<DataField, Value>) -> Option<bool> {
        data.extract::<bool>(DataField::LightFlashing)
    }
}

impl GetMessages for MaraV1 {
    fn parse_messages(&self, data: &HashMap<DataField, Value>) -> Vec<MinerMessage> {
        let messages = data.get(&DataField::Messages).and_then(|v| v.as_array());
        let mut result = vec![];
        if let Some(m) = messages {
            for message in m {
                let level = if let Some(level) = message.get("level").and_then(|v| v.as_str()) {
                    match level {
                        "info" => MessageSeverity::Info,
                        "warning" => MessageSeverity::Warning,
                        "error" => MessageSeverity::Error,
                        _ => MessageSeverity::Info,
                    }
                } else {
                    MessageSeverity::Info
                };

                let message_text = message
                    .get("message")
                    .and_then(|v| v.as_str())
                    .unwrap_or("")
                    .to_string();
                let timestamp = message
                    .get("timestamp")
                    .and_then(|v| v.as_u64())
                    .unwrap_or(0);

                let m_msg = MinerMessage {
                    timestamp: timestamp as u32,
                    code: 0,
                    message: message_text,
                    severity: level,
                };

                result.push(m_msg);
            }
        }

        result
    }
}
impl GetUptime for MaraV1 {
    fn parse_uptime(&self, data: &HashMap<DataField, Value>) -> Option<Duration> {
        data.extract::<u64>(DataField::Uptime)
            .map(Duration::from_secs)
    }
}

impl GetIsMining for MaraV1 {
    fn parse_is_mining(&self, data: &HashMap<DataField, Value>) -> bool {
        data.extract::<String>(DataField::IsMining)
            .map(|status| status == "Mining")
            .unwrap_or(false)
    }
}

impl GetPools for MaraV1 {
    fn parse_pools(&self, data: &HashMap<DataField, Value>) -> Vec<PoolData> {
        let mut pools_vec: Vec<PoolData> = Vec::new();

        if let Some(pools_data) = data.get(&DataField::Pools)
            && let Some(pools_array) = pools_data.as_array()
        {
            let mut active_pool_index = None;
            let mut highest_priority = i32::MAX;

            for pool_info in pools_array {
                if let (Some(status), Some(priority), Some(index)) = (
                    pool_info.get("status").and_then(|v| v.as_str()),
                    pool_info.get("priority").and_then(|v| v.as_i64()),
                    pool_info.get("index").and_then(|v| v.as_u64()),
                ) && status == "Alive"
                    && (priority as i32) < highest_priority
                {
                    highest_priority = priority as i32;
                    active_pool_index = Some(index as u16);
                }
            }

            for pool_info in pools_array {
                let url = pool_info
                    .get("url")
                    .and_then(|v| v.as_str())
                    .filter(|s| !s.is_empty())
                    .map(|s| PoolURL::from(s.to_string()));

                let index = pool_info
                    .get("index")
                    .and_then(|v| v.as_u64())
                    .map(|i| i as u16);
                let user = pool_info
                    .get("user")
                    .and_then(|v| v.as_str())
                    .map(String::from);
                let accepted = pool_info.get("accepted").and_then(|v| v.as_u64());
                let rejected = pool_info.get("rejected").and_then(|v| v.as_u64());
                let active = index.map(|i| Some(i) == active_pool_index).unwrap_or(false);
                let alive = pool_info
                    .get("status")
                    .and_then(|v| v.as_str())
                    .map(|s| s == "Alive");

                pools_vec.push(PoolData {
                    position: index,
                    url,
                    accepted_shares: accepted,
                    rejected_shares: rejected,
                    active: Some(active),
                    alive,
                    user,
                });
            }
        }

        pools_vec
    }
}

#[async_trait]
impl SetFaultLight for MaraV1 {
    #[allow(unused_variables)]
    async fn set_fault_light(&self, fault: bool) -> Result<bool> {
        bail!("Unsupported command");
    }
}

#[async_trait]
impl SetPowerLimit for MaraV1 {
    #[allow(unused_variables)]
    async fn set_power_limit(&self, limit: Power) -> Result<bool> {
        bail!("Unsupported command");
    }
}

#[async_trait]
impl Restart for MaraV1 {
    async fn restart(&self) -> Result<bool> {
        bail!("Unsupported command");
    }
}

#[async_trait]
impl Pause for MaraV1 {
    #[allow(unused_variables)]
    async fn pause(&self, at_time: Option<Duration>) -> Result<bool> {
        bail!("Unsupported command");
    }
}

#[async_trait]
impl Resume for MaraV1 {
    #[allow(unused_variables)]
    async fn resume(&self, at_time: Option<Duration>) -> Result<bool> {
        bail!("Unsupported command");
    }
}
