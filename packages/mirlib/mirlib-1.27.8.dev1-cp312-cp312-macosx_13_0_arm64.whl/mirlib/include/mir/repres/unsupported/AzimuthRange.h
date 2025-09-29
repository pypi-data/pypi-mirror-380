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

#include "mir/repres/Gridded.h"


namespace mir::repres::unsupported {


class AzimuthRange final : public Gridded {
public:
    // -- Exceptions
    // None

    // -- Constructors

    explicit AzimuthRange(const param::MIRParametrisation&);

    AzimuthRange(const AzimuthRange&) = delete;
    AzimuthRange(AzimuthRange&&)      = delete;

    // -- Destructor
    // None

    // -- Convertors
    // None

    // -- Operators

    AzimuthRange& operator=(const AzimuthRange&) = delete;
    AzimuthRange& operator=(AzimuthRange&&)      = delete;

    // -- Methods
    // // None

    // -- Overridden methods
    // None

    // -- Class members
    // None

    // -- Class methods
    // None

protected:
    // -- Members
    // None

    // -- Methods

    void print(std::ostream&) const override;

    // -- Overridden methods
    // None

    // -- Class members
    // None

    // -- Class methods
    // None

private:
    // -- Members
    // None

    // -- Methods
    // None

    // -- Overridden methods
    // None

    // -- Class members
    // None

    // -- Class methods
    // None

    // -- Friends
    // None
};


}  // namespace mir::repres::unsupported
