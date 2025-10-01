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

#include "mir/output/GribOutput.h"


namespace eckit {
class DataHandle;
}


namespace mir::output {


class GribStreamOutput : public GribOutput {
public:
    // -- Exceptions
    // None

    // -- Constructors

    GribStreamOutput();

    // -- Destructor

    ~GribStreamOutput() override;

    // -- Convertors
    // None

    // -- Operators
    // None

    // -- Methods
    // None

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


    // -- Overridden methods
    // None

    // -- Class members
    // None

    // -- Class methods
    // None

private:
    // -- Members

    // -- Methods

    virtual eckit::DataHandle& dataHandle() = 0;

    // -- Overridden methods
    // From MIROutput

    void out(const void* message, size_t length, bool interpolated) override;

    // -- Class members
    // None

    // -- Class methods
    // None

    // -- Friends
    // None
};


}  // namespace mir::output
