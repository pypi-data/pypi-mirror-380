#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "reading/straw.cpp"

namespace py = pybind11;



class PyReader {
    std::unique_ptr<HiCFile> hic_file;

public:
    std::vector<int32_t> bin_sizes;
    py::dict chr_sizes;

    PyReader(const std::string &path) {
        hic_file = std::make_unique<HiCFile>(path);

        bin_sizes = hic_file->getResolutions();
        std::sort(bin_sizes.begin(), bin_sizes.end());

        for (const auto &chr_entry : hic_file->getChromosomes()) {
            if (chr_entry.name == "All") continue;
            chr_sizes[py::str(chr_entry.name)] = chr_entry.length;
        }
    }

    py::array_t<float> read_signal(
        const std::vector<std::string> &chr_ids,
        const std::vector<int64_t> &starts,
        const std::vector<int64_t> &ends,
        int32_t bin_size = -1,
        std::string mode = "observed",
        std::string normalization = "none",
        std::string unit = "bp"
    ) {
        
        if (chr_ids.size() != 2 || starts.size() != 2 || ends.size() != 2) {
            throw std::runtime_error("chr_ids, starts and ends must each have 2 elements");
        }
        if (bin_size <= 0) bin_size = bin_sizes.front();
        std::transform(mode.begin(), mode.end(), mode.begin(), ::tolower);
        std::transform(normalization.begin(), normalization.end(), normalization.begin(), ::toupper);
        std::transform(unit.begin(), unit.end(), unit.begin(), ::toupper);

        auto mzd = hic_file->getMatrixZoomData(chr_ids[0], chr_ids[1], mode, normalization, unit, bin_size);
        auto data = mzd->getRecordsAsMatrix(starts[0], ends[0], starts[1], ends[1]);

        int32_t row_count = (ends[0] - starts[0]) / bin_size;
        int32_t col_count = (ends[1] - starts[1]) / bin_size;
        return py::array_t<float>(
            {row_count, col_count}, // shape
            {col_count * sizeof(float), sizeof(float)}, // strides
            data.data() // data pointer
        );

    }

    py::dict read_sparse_signal(
        const std::vector<std::string> &chr_ids,
        const std::vector<int64_t> &starts,
        const std::vector<int64_t> &ends,
        int32_t bin_size = -1,
        std::string mode = "observed",
        std::string normalization = "none",
        std::string unit = "bp"
    ) {
        
        if (chr_ids.size() != 2 || starts.size() != 2 || ends.size() != 2) {
            throw std::runtime_error("chr_ids, starts and ends must each have 2 elements");
        }
        if (bin_size <= 0) bin_size = bin_sizes.front();
        std::transform(mode.begin(), mode.end(), mode.begin(), ::tolower);
        std::transform(normalization.begin(), normalization.end(), normalization.begin(), ::toupper);
        std::transform(unit.begin(), unit.end(), unit.begin(), ::toupper);

        auto mzd = hic_file->getMatrixZoomData(chr_ids[0], chr_ids[1], mode, normalization, unit, bin_size);
        auto data = mzd->getRecordsAsSparseMatrix(starts[0], ends[0], starts[1], ends[1]);

        py::dict result;
        result["data"] = py::array_t<float>(data.data.size(), data.data.data());
        result["row"] = py::array_t<int32_t>(data.row.size(), data.row.data());
        result["col"] = py::array_t<int32_t>(data.col.size(), data.col.data());
        result["shape"] = py::make_tuple(std::get<0>(data.shape), std::get<1>(data.shape));
        return result;

    }



    


};

PYBIND11_MODULE(hic_io, m, py::mod_gil_not_used()) {
    m.doc() = "Python bindings for hic_io C++ library";

    py::class_<PyReader>(m, "Reader")
        .def(py::init<const std::string&>(), "Hic file reader",
            py::arg("path"))
        .def_readonly("bin_sizes", &PyReader::bin_sizes)
        .def_readonly("chr_sizes", &PyReader::chr_sizes)
        .def("read_signal", &PyReader::read_signal,
            "Read signal",
            py::arg("chr_ids"),
            py::arg("starts"),
            py::arg("ends"),
            py::arg("bin_size") = -1,
            py::arg("mode") = "observed",
            py::arg("normalization") = "none",
            py::arg("unit") = "bp"
        )
        .def("read_sparse_signal", &PyReader::read_sparse_signal,
            "Read sparse signal",
            py::arg("chr_ids"),
            py::arg("starts"),
            py::arg("ends"),
            py::arg("bin_size") = -1,
            py::arg("mode") = "observed",
            py::arg("normalization") = "none",
            py::arg("unit") = "bp"
        );

}
