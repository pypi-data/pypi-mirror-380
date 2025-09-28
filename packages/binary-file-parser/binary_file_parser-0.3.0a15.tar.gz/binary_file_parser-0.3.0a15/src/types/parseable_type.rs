use std::cmp::Ordering;
use pyo3::{Bound, IntoPy, PyAny, PyResult, Python};
use pyo3::types::PyBytes;
use serde::{Serialize, Serializer};
use crate::{impl_from_for_parseable_type, impl_try_into_for_parseable_type};
use crate::types::base_struct::BaseStruct;
use crate::types::bfp_list::BfpList;
use crate::types::bfp_type::BfpType;
use crate::types::r#struct::Struct;
use crate::types::serial::struct_serializer::StructSerializer;

// todo: change to structural enum
#[derive(Debug, Clone)]
pub enum ParseableType {
    None,
    UInt8(u8),
    UInt16(u16),
    UInt32(u32),
    UInt64(u64),
    UInt128(u128),
    
    Int8(i8),
    Int16(i16),
    Int32(i32),
    Int64(i64),
    Int128(i128),

    Float32(f32),
    Float64(f64),

    Bool(bool),
    
    Str(String),
    
    Array(BfpList),
    
    Bytes(Vec<u8>),
    
    Option(Option<Box<ParseableType>>),
    
    Struct { val: BaseStruct, struct_: Struct },
}

impl ParseableType {
    pub fn is_ls_of(&self, bfp_type: &BfpType) -> bool {
        match self {
            ParseableType::Array(val) => {
                let inner = val.inner();
                inner.data_type == *bfp_type
            },
            _ => false,
        }
    }
    
    /// converts ParseableTypes back to python values
    pub fn to_bound(self, py: Python) -> PyResult<Bound<'_, PyAny>> {
        match self {
            ParseableType::None                         => Ok(py.None().into_bound(py)),
            ParseableType::UInt8(val)                   => Ok(val.into_py(py).into_bound(py)),
            ParseableType::UInt16(val)                  => Ok(val.into_py(py).into_bound(py)),
            ParseableType::UInt32(val)                  => Ok(val.into_py(py).into_bound(py)),
            ParseableType::UInt64(val)                  => Ok(val.into_py(py).into_bound(py)),
            ParseableType::UInt128(val)                 => Ok(val.into_py(py).into_bound(py)),

            ParseableType::Int8(val)                    => Ok(val.into_py(py).into_bound(py)),
            ParseableType::Int16(val)                   => Ok(val.into_py(py).into_bound(py)),
            ParseableType::Int32(val)                   => Ok(val.into_py(py).into_bound(py)),
            ParseableType::Int64(val)                   => Ok(val.into_py(py).into_bound(py)),
            ParseableType::Int128(val)                  => Ok(val.into_py(py).into_bound(py)),

            ParseableType::Float32(val)                 => Ok(val.into_py(py).into_bound(py)),
            ParseableType::Float64(val)                 => Ok(val.into_py(py).into_bound(py)),

            ParseableType::Bool(val)                    => Ok(val.into_py(py).into_bound(py)),

            ParseableType::Str(val)                     => Ok(val.into_py(py).into_bound(py)),

            ParseableType::Array(val)                   => Ok(val.into_py(py).into_bound(py)),

            ParseableType::Bytes(val)                   => Ok(PyBytes::new_bound(py, &val).into_any()),

            ParseableType::Option(val)                  => { 
                match val {
                    None      => Ok(py.None().into_bound(py)),
                    Some(val) => val.to_bound(py),
                }
            },

            ParseableType::Struct { val, struct_ }      => {
                let inner = val.inner();
                match inner.obj.get() {
                    None => {
                        let obj = BaseStruct::with_cls(val.clone(), struct_.py_type(py))?;
                        inner.obj.set(obj.clone().unbind()).expect("infallible");
                        Ok(obj)
                    }
                    Some(obj) => {
                        Ok(obj.bind(py).clone())
                    }
                }
            },
        }
    }
    
    pub fn try_to_int(&self) -> Option<i128> {
        match self {
            ParseableType::UInt8(val)   => Some(*val as i128),
            ParseableType::UInt16(val)  => Some(*val as i128),
            ParseableType::UInt32(val)  => Some(*val as i128),
            ParseableType::UInt64(val)  => Some(*val as i128),
            ParseableType::UInt128(val) => Some(*val as i128),

            ParseableType::Int8(val)    => Some(*val as i128),
            ParseableType::Int16(val)   => Some(*val as i128),
            ParseableType::Int32(val)   => Some(*val as i128),
            ParseableType::Int64(val)   => Some(*val as i128),
            ParseableType::Int128(val)  => Some(*val),
            
            _ => None,
        }
    }
    
    pub fn try_to_float(&self) -> Option<f64> {
        match self {
            ParseableType::Float32(val) => Some(*val as f64),
            ParseableType::Float64(val) => Some(*val),

            _ => None,
        }
    }
    
    pub fn try_len(&self) -> Option<usize> {
        match self {
            ParseableType::Array(ls) => Some(ls.len()),
            _ => None,
        }
    }
}

impl PartialOrd for ParseableType {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        match (self.try_to_int(), other.try_to_int()) {
            (Some(num1), Some(num2))          => return num1.partial_cmp(&num2),
            (Some(_), None) | (None, Some(_)) => return None,
            _ => {}
        };

        match (self.try_to_float(), other.try_to_float()) {
            (Some(num1), Some(num2))          => return num1.partial_cmp(&num2),
            (Some(_), None) | (None, Some(_)) => return None,
            _ => {}
        };

        match (self, other) { // todo fix
            (ParseableType::None,          ParseableType::None)          => Some(Ordering::Equal),
            (ParseableType::Bool(val1),    ParseableType::Bool(val2))    => val1.partial_cmp(&val2),
            (ParseableType::Str(val1),     ParseableType::Str(val2))     => val1.partial_cmp(&val2),
            (ParseableType::Array(val1),   ParseableType::Array(val2))   => val1.partial_cmp(&val2),
            (ParseableType::Bytes(val1),   ParseableType::Bytes(val2))   => val1.partial_cmp(&val2),
            (ParseableType::Option(val1),  ParseableType::Option(val2))  => val1.partial_cmp(&val2),
            (ParseableType::Struct { .. }, ParseableType::Struct { .. }) => None,
            _                                                            => None
        }
    }
}

impl PartialEq for ParseableType {
    fn eq(&self, other: &Self) -> bool {
        match (self.try_to_int(), other.try_to_int()) {
            (Some(num1), Some(num2))          => return num1 == num2,
            (Some(_), None) | (None, Some(_)) => return false,
            _ => {}
        };

        match (self.try_to_float(), other.try_to_float()) {
            (Some(num1), Some(num2))          => return num1 == num2,
            (Some(_), None) | (None, Some(_)) => return false,
            _ => {}
        };
        
        match (self, other) { // todo fix
            (ParseableType::None,                     ParseableType::None)                     => true,
            (ParseableType::Bool(val1),               ParseableType::Bool(val2))               => val1 == val2,
            (ParseableType::Str(val1),                ParseableType::Str(val2))                => val1 == val2,
            (ParseableType::Array(val1),              ParseableType::Array(val2))              => val1 == val2,
            (ParseableType::Bytes(val1),              ParseableType::Bytes(val2))              => val1 == val2,
            (ParseableType::Option(val1),             ParseableType::Option(val2))             => val1 == val2,
            (ParseableType::Struct { val: val1, .. }, ParseableType::Struct { val: val2, .. }) => val1 == val2,
            _                                                                                  => false
        }
    }
}

impl Eq for ParseableType {}

impl_try_into_for_parseable_type!(isize);
impl_try_into_for_parseable_type!(usize);

impl_from_for_parseable_type!(u8, UInt8);
impl_from_for_parseable_type!(u16, UInt16);
impl_from_for_parseable_type!(u32, UInt32);
impl_from_for_parseable_type!(u64, UInt64);
impl_from_for_parseable_type!(u128, UInt128);

impl_from_for_parseable_type!(i8, Int8);
impl_from_for_parseable_type!(i16, Int16);
impl_from_for_parseable_type!(i32, Int32);
impl_from_for_parseable_type!(i64, Int64);
impl_from_for_parseable_type!(i128, Int128);

impl_from_for_parseable_type!(f32, Float32);
impl_from_for_parseable_type!(f64, Float64);

impl_from_for_parseable_type!(bool, Bool);

impl_from_for_parseable_type!(String, Str);

impl_from_for_parseable_type!(BfpList, Array);

impl_from_for_parseable_type!(Vec<u8>, Bytes);

impl_from_for_parseable_type!(Option<Box<ParseableType>>, Option);

impl Serialize for ParseableType {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer
    {
        match self {
            ParseableType::None => serializer.serialize_none(),

            ParseableType::UInt8(v) => serializer.serialize_u8(*v),
            ParseableType::UInt16(v) => serializer.serialize_u16(*v),
            ParseableType::UInt32(v) => serializer.serialize_u32(*v),
            ParseableType::UInt64(v) => serializer.serialize_u64(*v),
            ParseableType::UInt128(v) => serializer.serialize_u128(*v),

            ParseableType::Int8(v) => serializer.serialize_i8(*v),
            ParseableType::Int16(v) => serializer.serialize_i16(*v),
            ParseableType::Int32(v) => serializer.serialize_i32(*v),
            ParseableType::Int64(v) => serializer.serialize_i64(*v),
            ParseableType::Int128(v) => serializer.serialize_i128(*v),

            ParseableType::Float32(v) => serializer.serialize_f32(*v),
            ParseableType::Float64(v) => serializer.serialize_f64(*v),

            ParseableType::Bool(v) => serializer.serialize_bool(*v),

            ParseableType::Str(s) => serializer.serialize_str(s),

            ParseableType::Array(arr) => arr.serialize(serializer),

            ParseableType::Bytes(bytes) => serializer.serialize_bytes(bytes),

            ParseableType::Option(opt) => opt.serialize(serializer),

            ParseableType::Struct { val, struct_, .. } => {
                StructSerializer(struct_, val).serialize(serializer)
            }
        }
    }
}