/*
 * (C) Copyright 1996- ECMWF.
 *
 * This software is licensed under the terms of the Apache Licence Version 2.0
 * which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
 *
 * In applying this licence, ECMWF does not waive the privileges and immunities
 * granted to it by virtue of its status as an intergovernmental organisation nor
 * does it submit to any jurisdiction.
 */


#pragma once

#include <vector>

#include "eckit/types/Fraction.h"

#include "mir/repres/Iterator.h"
#include "mir/util/BoundingBox.h"


namespace mir::repres::gauss {


class GaussianIterator : public Iterator {
public:
    GaussianIterator(const std::vector<double>& latitudes, std::vector<long>&& pl, const util::BoundingBox&, size_t N,
                     size_t Nj, size_t k, const util::Rotation& = util::Rotation());
    ~GaussianIterator() override;

private:
    const std::vector<double>& latitudes_;
    const std::vector<long> pl_;
    const util::BoundingBox& bbox_;
    const size_t N_;
    size_t Ni_;
    size_t Nj_;
    eckit::Fraction lon_;
    Latitude lat_;
    eckit::Fraction inc_;
    size_t i_;
    size_t j_;
    size_t k_;
    size_t count_;
    bool first_;

protected:
    void print(std::ostream&) const override;
    bool next(Latitude&, Longitude&) override;
    size_t index() const override;
    size_t resetToRow(size_t j);
};


}  // namespace mir::repres::gauss
