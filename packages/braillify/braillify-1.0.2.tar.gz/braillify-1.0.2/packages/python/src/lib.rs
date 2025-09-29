use braillify as braillify_core;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

#[pyfunction]
fn encode(text: &str) -> PyResult<Vec<u8>> {
    braillify_core::encode(text).map_err(PyErr::new::<PyValueError, _>)
}

#[pyfunction]
fn translate_to_unicode(text: &str) -> PyResult<String> {
    braillify_core::encode_to_unicode(text).map_err(PyErr::new::<PyValueError, _>)
}

#[pyfunction]
fn translate_to_braille_font(text: &str) -> PyResult<String> {
    braillify_core::encode_to_braille_font(text).map_err(PyErr::new::<PyValueError, _>)
}

/// A Python module implemented in Rust.
#[pymodule(name = "braillify")]
fn lib_braillify(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode, m)?)?;
    m.add_function(wrap_pyfunction!(translate_to_unicode, m)?)?;
    m.add_function(wrap_pyfunction!(translate_to_braille_font, m)?)?;
    Ok(())
}
