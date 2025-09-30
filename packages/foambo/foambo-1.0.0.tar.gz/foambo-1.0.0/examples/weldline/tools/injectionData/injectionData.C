/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | foam-extend: Open Source CFD
   \\    /   O peration     | Version:     5.0
    \\  /    A nd           | Web:         http://www.foam-extend.org
     \\/     M anipulation  | For copyright notice see file Copyright
-------------------------------------------------------------------------------
License
    This file is part of foam-extend.

    foam-extend is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or (at your
    option) any later version.

    foam-extend is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with foam-extend.  If not, see <http://www.gnu.org/licenses/>.

Application
    injectionData

Description

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scalarList segmoidPulse(scalarList t, scalar amplitude, scalar t0, scalar k) {
    return amplitude / (1 + Foam::exp(k*(t-t0)));
}

int main(int argc, char *argv[])
{
    #include "setRootCase.H"
    #include "createTime.H"

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    IOdictionary gateSettings
    (
        IOobject
        (
            "gateSettings",
            runTime.constant(),
            runTime,
            IOobject::MUST_READ,
            IOobject::NO_WRITE
        )
    );

    scalar machineRampFactor = readScalar(gateSettings.lookup("machineRampFactor"));
    scalar flowRateScale = readScalar(gateSettings.lookup("flowRateScale"));

    for(int i = 1; i <= 4; i++) {
        dictionary gate = gateSettings.subDict(word("gate") + Foam::name(i));
        scalarList times(101);
        forAll(times, t) {
            times[t] = t*6.0/100;
        }
        scalar amp = readScalar(gate.lookup("injectionRate"));
        scalar t0 = readScalar(gate.lookup("injectionToggleTime"));
        bool initState = Switch(gate.lookup("injectionInitialState"));
        scalar k = -machineRampFactor;
        if (initState) k = -k;
        scalarList values = segmoidPulse(times, amp, t0, k);

        IOdictionary gateData
        (
            IOobject
            (
                word("gateData")+Foam::name(i),
                runTime.constant(),
                runTime,
                IOobject::NO_READ,
                IOobject::NO_WRITE
            )
        );
        OFstream os(runTime.caseConstant()+word("/gateInjection")+Foam::name(i)+".dat");
        if (Pstream::master()) {
            os << "(" << nl;
            forAll(values, vi) {
                if (os.opened()) {
                    os << "( " << times[vi] << " " << flowRateScale*values[vi] << " )" << nl;
                }
            }
            os << ")" << endl;
        }
    }

    Info<< nl << "ExecutionTime = " << runTime.elapsedCpuTime() << " s"
        << "  ClockTime = " << runTime.elapsedClockTime() << " s"
        << nl << endl;

    Info<< "End\n" << endl;

    return 0;
}


// ************************************************************************* //
