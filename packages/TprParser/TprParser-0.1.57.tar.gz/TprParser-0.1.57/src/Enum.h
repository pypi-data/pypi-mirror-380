#ifndef ENUM_H
#define ENUM_H

#if defined(_MSC_VER) || defined(_WIN32)
#    include <string.h>
#    define mystricmp _stricmp
#else
#    include <strings.h>
#    define mystricmp strcasecmp
#endif

enum class PbcType : int
{
    Xyz     = 0, //!< Periodic boundaries in all dimensions.
    No      = 1, //!< No periodic boundaries.
    XY      = 2, //!< Only two dimensions are periodic.
    Screw   = 3, //!< Screw.
    Unset   = 4, //!< The type of PBC is not set or invalid.
    Count   = 5,
    Default = Xyz
};

//< pressure coupling methods
enum class PressureCoupling : int
{
    No,
    Berendsen,
    ParrinelloRahman,
    Isotropic,
    Mttk,
    CRescale,
    Count
};
static const char* c_PressureCoupling[] =
    {"No", "Berendsen", "ParrinelloRahman", "Isotropic", "Mttk", "CRescale"};

//< pressure coupling type
enum class PressureCouplingType : int
{
    Isotropic,
    SemiIsotropic,
    Anisotropic,
    Count
};
static const char* c_PressureCouplingType[] = {"Isotropic", "SemiIsotropic", "Anisotropic"};

//< temperature coupling methods
enum class TemperatureCoupling : int
{
    No,
    Berendsen,
    NoseHoover,
    Yes,
    Andersen,
    AndersenMassive,
    VRescale,
    Count,
};
static const char* c_TemperatureCoupling[] =
    {"No", "Berendsen", "NoseHoover", "Yes", "Andersen", "AndersenMassive", "VRescale"};


// Integer mdp
enum class ParamsInteger : int
{
    nstlog,
    nstxout,
    nstvout,
    nstfout,
    nstenergy,
    nstxout_compressed,
    nsttcouple,
    nstpcouple,
    nstcalcenergy,
    nstlist,
    nstcomm,
    Count,
};
static const char* c_mdp_integer[] = {"nstlog",
                                      "nstxout",
                                      "nstvout",
                                      "nstfout",
                                      "nstenergy",
                                      "nstxout_compressed",
                                      "nsttcouple",
                                      "nstpcouple",
                                      "nstcalcenergy",
                                      "nstlist",
                                      "nstcomm"};

// vector of tpr, X or V or F
enum class VecProps : int
{
    x,
    v,
    f,
    m,   // the mass of atoms
    q,   // the charge of atoms
    box, // the box vector
    ef,  // electric field
    Count
};
static const char* c_mdp_vector[] = {"x", "v", "f", "m", "q", "box", "ef"};

// int vector of tpr, such resid
enum class IVectorProps : int
{
    resid,
    atnum,     // atomtype number
    atomicnum, // atomic number
    Count
};
static const char* c_int_vector[] = {"resid", "atnum", "atomicnum"};

// vector of tpr, resname / atomname / atomtype name
enum class StringType : int
{
    res,
    atom,
    type, // atomtype name
    Count
};
static const char* c_name_vector[] = {"res", "atom", "type"};


// type of bonded
enum class BondedType : int
{
    bonds,
    angles,
    dihedrals,
    impropers,
    Count
};
static const char* c_bonded_type[] = {"bonds", "angles", "dihedrals", "impropers"};

//< Non bonded type
enum class NonBondedType : int
{
    LJ,
    atomtype, // only [ atomtypes ]
    LJ_14,    // that is [ pairs ]
    Count
};
static const char* c_nonbonded_type[] = {"lj", "type", "pairs"};


//< check key words in a c_string array ignore case, return enum value if find, else return ENUM::Count
template<typename ENUM, const int count = static_cast<int>(ENUM::Count), int N>
static inline ENUM check_string(const char* str, const char* (&arr)[N])
{
    //! check length must be equal
    static_assert(N == count, "c_string length is not equal to enum length");
    for (int i = 0; i < count; i++)
    {
        if (!mystricmp(str, arr[i])) return static_cast<ENUM>(i);
    }
    return ENUM::Count;
}


//! Pulling algorithm.
enum class PullingAlgorithm : int
{
    Umbrella,
    Constraint,
    ConstantForce,
    FlatBottom,
    FlatBottomHigh,
    External,
    Count,
    Default = Umbrella
};

//! Control of pull groups
enum class PullGroupGeometry : int
{
    Distance,
    Direction,
    Cylinder,
    DirectionPBC,
    DirectionRelative,
    Angle,
    Dihedral,
    AngleAxis,
    Transformation,
    Count,
    Default = Distance
};


//! Enforced rotation group type.
enum class EnforcedRotationGroupType : int
{
    Iso,
    Isopf,
    Pm,
    Pmpf,
    Rm,
    Rmpf,
    Rm2,
    Rm2pf,
    Flex,
    Flext,
    Flex2,
    Flex2t,
    Count,
    Default = Iso
};

//! Rotation group fitting type
enum class RotationGroupFitting : int
{
    Rmsd,
    Norm,
    Pot,
    Count,
    Default = Rmsd
};

#endif // !ENUM_H
