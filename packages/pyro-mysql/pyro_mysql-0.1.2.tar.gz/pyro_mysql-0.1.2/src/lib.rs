#![allow(async_fn_in_trait)]

pub mod r#async;
pub mod capability_flags;
pub mod error;
pub mod isolation_level;
pub mod params;
pub mod row;
pub mod sync;
pub mod util;
pub mod value;

use pyo3::prelude::*;
use tokio::runtime::Builder;

use crate::{
    r#async::{
        AsyncOpts, AsyncOptsBuilder, AsyncPoolOpts, conn::AsyncConn, pool::AsyncPool,
        transaction::AsyncTransaction,
    },
    capability_flags::CapabilityFlags,
    isolation_level::IsolationLevel,
    row::Row,
    sync::{
        SyncConn, SyncPool, SyncPoolOpts, SyncPooledConn, SyncTransaction,
        opts::{SyncOpts, SyncOptsBuilder},
    },
    util::PyroFuture,
};

#[pyfunction]
/// This function can be called multiple times until any async operation is called.
#[pyo3(signature = (worker_threads=Some(1), thread_name=None))]
fn init(worker_threads: Option<usize>, thread_name: Option<&str>) {
    let mut builder = Builder::new_multi_thread();
    builder.enable_all();
    if let Some(n) = worker_threads {
        builder.worker_threads(n);
    }
    if let Some(name) = thread_name {
        builder.thread_name(name);
    }
    pyo3_async_runtimes::tokio::init(builder);
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyro_mysql(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    pyo3_log::init(); // the default filter uses DEBUG

    if cfg!(debug_assertions) {
        log::debug!("Running in Debug mode.");
    } else {
        log::debug!("Running in Release mode.");
    }

    init(Some(1), None);
    m.add_function(wrap_pyfunction!(init, m)?)?;
    m.add_class::<Row>()?;
    m.add_class::<IsolationLevel>()?;
    m.add_class::<CapabilityFlags>()?;
    m.add_class::<PyroFuture>()?;

    m.add_class::<AsyncPool>()?;
    m.add_class::<AsyncConn>()?;
    m.add_class::<AsyncTransaction>()?;
    m.add_class::<AsyncOpts>()?;
    m.add_class::<AsyncOptsBuilder>()?;
    m.add_class::<AsyncPoolOpts>()?;

    m.add_class::<SyncConn>()?;
    m.add_class::<SyncPool>()?;
    m.add_class::<SyncPooledConn>()?;
    m.add_class::<SyncPoolOpts>()?;
    m.add_class::<SyncTransaction>()?;
    m.add_class::<SyncOpts>()?;
    m.add_class::<SyncOptsBuilder>()?;

    // error
    let error = PyModule::new(py, "error")?;
    error.add(
        "IncorrectApiUsageError",
        py.get_type::<error::IncorrectApiUsageError>(),
    )?;
    error.add("UrlError", py.get_type::<error::UrlError>())?;
    error.add("MysqlError", py.get_type::<error::MysqlError>())?;
    error.add(
        "ConnectionClosedError",
        py.get_type::<error::ConnectionClosedError>(),
    )?;
    error.add(
        "TransactionClosedError",
        py.get_type::<error::TransactionClosedError>(),
    )?;
    error.add(
        "BuilderConsumedError",
        py.get_type::<error::BuilderConsumedError>(),
    )?;
    error.add("DecodeError", py.get_type::<error::DecodeError>())?;
    pyo3::py_run!(
        py,
        error,
        "import sys; sys.modules['pyro_mysql.error'] = error"
    );
    m.add_submodule(&error)?;

    // async
    let async_ = PyModule::new(py, "async_")?;
    async_.add("Pool", py.get_type::<AsyncPool>())?;
    async_.add("Conn", py.get_type::<AsyncConn>())?;
    async_.add("Transaction", py.get_type::<AsyncTransaction>())?;
    async_.add("Opts", py.get_type::<AsyncOpts>())?;
    async_.add("OptsBuilder", py.get_type::<AsyncOptsBuilder>())?;
    async_.add("PoolOpts", py.get_type::<AsyncPoolOpts>())?;
    m.add_submodule(&async_)?;
    pyo3::py_run!(
        py,
        async_,
        "import sys; sys.modules['pyro_mysql.async_'] = async_"
    );

    // sync
    let sync = PyModule::new(py, "sync")?;
    sync.add("Conn", py.get_type::<SyncConn>())?;
    sync.add("Pool", py.get_type::<SyncPool>())?;
    sync.add("PooledConn", py.get_type::<SyncPooledConn>())?;
    sync.add("Opts", py.get_type::<SyncOpts>())?;
    sync.add("OptsBuilder", py.get_type::<SyncOptsBuilder>())?;
    sync.add("PoolOpts", py.get_type::<SyncPoolOpts>())?;
    sync.add(
        "ResultSetIterator",
        py.get_type::<sync::iterator::ResultSetIterator>(),
    )?;
    m.add_submodule(&sync)?;

    // a hack for Python's import system
    let sys_modules = py.import("sys")?.getattr("modules")?;
    sys_modules.set_item("pyro_mysql.async_", async_)?;
    sys_modules.set_item("pyro_mysql.sync", sync)?;
    sys_modules.set_item("pyro_mysql.error", error)?;

    Ok(())
}
