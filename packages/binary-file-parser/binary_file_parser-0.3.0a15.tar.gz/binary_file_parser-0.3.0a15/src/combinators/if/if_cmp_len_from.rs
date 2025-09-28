use std::cmp::Ordering;
use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;

use crate::combinators::combinator::Combinator;
use crate::combinators::combinator_type::CombinatorType;
use crate::combinators::utils::{get_rec};
use crate::retrievers::retriever::Retriever;
use crate::types::context::Context;
use crate::types::parseable_type::ParseableType;
use crate::types::version::Version;

#[pyclass(module = "bfp_rs.combinators")]
#[derive(Debug, Clone)]
pub struct IfCmpLenFrom {
    target: Vec<usize>,
    source: Vec<usize>,
    ord: Vec<Ordering>,
    coms: Vec<CombinatorType>,
}

impl IfCmpLenFrom {
    pub fn new(target: &Vec<usize>, source: &Vec<usize>, ord: &Vec<Ordering>, coms: Vec<CombinatorType>) -> Self {
        IfCmpLenFrom {
            target: target.clone(),
            source: source.clone(),
            ord: ord.clone(),
            coms,
        }
    }
}

impl Combinator for IfCmpLenFrom {
    fn run(
        &self,
        retrievers: &Vec<Retriever>,
        data: &mut Vec<Option<ParseableType>>,
        repeats: &mut Vec<Option<isize>>,
        ver: &Version,
        ctx: &mut Context,
    ) -> PyResult<()> {
        let (target_name, target) = get_rec(&self.target, retrievers, data, ver)?;
        let (source_name, source) = get_rec(&self.source, retrievers, data, ver)?;

        let Some(target) = target.try_len() else {
            return Err(PyTypeError::new_err(format!(
                "IfCmpLenFrom: '{}' cannot be interpreted as a list", target_name
            )))
        };
        let Ok(source) = (&source).try_into() else {
            return Err(PyTypeError::new_err(format!(
                "IfCmpLenFrom: '{}' cannot be interpreted as an integer", source_name
            )))
        };
        
        let ord = target.cmp(&source);
        
        ctx.enter_if();
        if self.ord.contains(&ord) {
            for com in &self.coms {
                com.run(retrievers, data, repeats, ver, ctx)?;
            }
            ctx.run_if();
        }
        Ok(())
    }
}
