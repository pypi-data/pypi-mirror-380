#ifndef TPRDATA_H
#define TPRDATA_H

#include <array>
#include <cassert>
#include <stdexcept>
#include <string>
#include <tuple> // std::tie
#include <utility>
#include <vector>

#include "define.h"
#include "Enum.h"

using vecI2D = std::vector<std::vector<int>>;
using vecF2D = std::vector<std::vector<float>>;
using vecU2D = std::vector<std::vector<unsigned short>>;


//< code can reach
static inline void unreachable()
{
#if HAS_BUILTIN_UNREACHABLE
    __builtin_unreachable();
#elif defined(_MSC_VER)
    __assume(false);
#else
    throw std::runtime_error("entered unreachable code");
#endif
}

// bonded pairs and ff parameters, such as bonds, angle, dihedrals
struct Bonded
{
    // bond
    Bonded(int ta, int tb, int functype, const std::vector<float>& ffparam)
        : a(ta), b(tb), ifunc(functype), ff{ffparam}
    {
        if (a > b) std::swap(a, b);
    }

    // angle
    Bonded(int ta, int tb, int tc, int functype, const std::vector<float>& ffparam)
        : a(ta), b(tb), c(tc), ifunc(functype), ff{ffparam}
    {
        if (a > c) std::swap(a, c);
    }

    // dihedral
    Bonded(int ta, int tb, int tc, int td, int functype, const std::vector<float>& ffparam)
        : a(ta), b(tb), c(tc), d(td), ifunc(functype), ff{ffparam}
    {
        // small x x big
        if (a > d)
        {
            std::swap(a, d);
            std::swap(b, c);
        }
    }

    // return a, b, c, d according to index 0-3
    int& operator[](size_t idx)
    {
        assert(idx >= 0 && idx < 4);
        switch (idx)
        {
            case 0: return a;
            case 1: return b;
            case 2: return c;
            case 3: return d;
        }
        unreachable();
    }
    // const version
    int operator[](size_t idx) const
    {
        assert(idx >= 0 && idx < 4);
        switch (idx)
        {
            case 0: return a;
            case 1: return b;
            case 2: return c;
            case 3: return d;
        }
        unreachable();
    }

    // ��ȥ�ظ���vector
    // a b c d
    // bool operator<(const Bonded& rhs) const
    //{
    //	return std::tie(a, d, b, c) < std::tie(rhs.a, rhs.d, rhs.b, rhs.c);
    //}

    int                a     = 0; // atom1
    int                b     = 0; // atom2
    int                c     = 0; // atom3
    int                d     = 0; // atom4
    int                ifunc = 0; // the function type id, 1,2,,,
    std::vector<float> ff{};      // ff parameters
};

//< Non-Bonded pairs
struct NonBonded
{
    NonBonded() = default; // used for std::vector .resize()

    // pairs set
    NonBonded(int i, int j, int functype, const std::vector<float>& ffparam)
        : a(i), b(j), ifunc(functype), ff{ffparam}
    {
    }

    // LJ set
    NonBonded(int functype, const std::vector<float>& ffparam) : ifunc(functype), ff{ffparam} {}
    // LJ set by copy constructor
    NonBonded(const NonBonded& rhs) noexcept
    {
        a     = rhs.a;
        b     = rhs.b;
        ifunc = rhs.ifunc;
        ff    = rhs.ff;
    }

    int& operator[](size_t idx)
    {
        assert(idx >= 0 && idx < 2);
        return idx == 0 ? a : b;
    }

    // const version
    int operator[](size_t idx) const
    {
        assert(idx >= 0 && idx < 2);
        return idx == 0 ? a : b;
    }

    int                a     = 0; // atom1 of [ pairs ]
    int                b     = 0; // atom2 of [ pairs ]
    int                ifunc = 0;
    std::vector<float> ff{}; // non-bonded parameters
};


struct TprData
{
    // POD clear zero
    TprData() = default;

    ~TprData() {}

    int                prec;      //< the precision of tpr, 4 or 8
    int                filever;   //< the version of file format, fver
    int                vergen;    //< the verions of generation code, fgen
    int                natoms;    //< the total natoms
    int                ngtc;      //< The number of temperature coupling groups.
    int                fep_state; //< fep state
    float              lambda;    //< lambda
    bool               bIr;       //< if has ir
    bool               bTop;      //< if has top
    bool               bX;        //< if has coordinates
    bool               bV;        //< if has velocity
    bool               bF;        //< if has force
    bool               bBox;      //< if has box
    bool               bInter;    //< if has inter-molecular bonds
    std::vector<float> box = {};  //< box size
    std::vector<char>  symtab;    //< symb name, truncate to SAVELEN characters
    int                nmoltypes, nmolblock;
    int                atnr; // the number of LJ type

    std::vector<int> atomsinmol;
    std::vector<int> resinmol;
    std::vector<int> molnames;
    std::vector<int> molbtype;
    std::vector<int> molbnmol;
    std::vector<int> molbnatoms; //! ÿ���������ж��ٸ�ԭ�ӹ���, = atomsinmol
    vecF2D           charges;
    vecF2D           masses;
    vecI2D           resids;
    std::vector<int> trueresids; // actually residues number in tpr
    vecI2D           ptypes;
    vecU2D           types; // LJ param type id
    vecI2D           atomnameids;
    vecI2D           atomtypeids;
    vecI2D           resnames;
    vecI2D           atomicnumbers;

    struct Excls
    {
        std::array<int, 2> range; ///< list [start, end] positions, included end
        std::vector<int>   index; ///< atom index, 0-based, NOTE: the order has be sorted by gmx
    };
    //! atom exclusions list for each moltype
    std::vector<std::vector<Excls>> excls;

    // mdp parameters
    struct
    {
        PbcType pbc = PbcType::Unset; //< which pbc type
        bool    pbcmol;               //< periodic-molecules
        int64_t nsteps;               // the number of simulation steps
        int64_t init_step;            // simulation init steps
        int     simulation_part;
        int     nstcalcenergy;
        int     cutoff_scheme; // int to enum
        int     nstlist;
        int     nstcomm;
        int     comm_mode; // int to enum, 0=Linear, 1=Angular
        int nstcgsteep; // Number of steps after which a steepest descents step is done while doing cg
        int    nbfgscorr;          // Number of corrections to the Hessian to keep
        int    nstlog;             // number of log steps
        int    nstxout;            // number of trr coordinates steps
        int    nstvout;            // number of velocity steps
        int    nstfout;            // number of force steps
        int    nstenergy;          // number of energy output steps
        int    nstxout_compressed; // number of xtc coordinates steps
        double init_t = 0.0;       // init time, ps
        double dt     = 0.0;       // time steps, ps

        float x_compression_precision; /// precision of xtc coordinates
        float verletbuf_tol;           // tolerance of verlet buffer
        float verletBufferPressureTolerance;
        float rlist;
        int   coulombtype;      // int to enum, 0=Cut, 1=RF, 3=Pme
        int   coulomb_modifier; // int to enum, 0=PotShiftVerletUnsupported, 1=PotShift, 2=None
        float rcoulomb_switch;
        float rcoulomb;
        int   vdwtype;      // int to enum, 0=Cut, 1=Switch,2=Shift, ...
        int   vdw_modifier; // int to enum


        float rvdw_switch;
        float rvdw;
        int   eDispCorr;
        float epsilon_r;
        float epsilon_rf;
        float tabext;

        bool implicit_solvent = false; // if has implicit solvent

        float fourier_spacing;
        int   nkx;
        int   nky;
        int   nkz;
        int   pme_order;
        float ewald_rtol;
        float ewald_rtol_lj;
        int   ewald_geometry; // int to enum, 0=3D, 1=3DC
        float epsilon_surface;
        int   ljpme_combination_rule; // int to enum, 0=Geom, 1=LB
        bool  bContinuation;
        // int to enum, 0=No,1=Berendsen,2=NoseHoover,3=Yes,4=Andersen,5=AndersenMassive
        // 6=VRescale
        int etc;

        int nsttcouple;
        int nstpcouple;
        int epc; // Pressure coupling algorithm��int to enum, 0=No, 1=Berendsen, 2=ParrinelloRahman,5=CRescale
        int   epct; // Pressure coupling type, int to enum, 0=Isotropic, 1=SemiIsotropic
        float tau_p;
        float ref_p[DIM * DIM]    = {0};
        float compress[DIM * DIM] = {0};
        // can multiple com group
        std::vector<std::array<float, DIM>> posres_com;
        std::vector<std::array<float, DIM>> posres_comB;
        int                                 refcoord_scaling; // int to enum,0=No,1=All,2=Com

        float shake_tol;     // tolerance of shake
        int   efep;          // int to enum
        int   n_lambda = 0;  // The number of foreign lambda points
        bool  bSimTemp;      // if has simulation temperature
        int   eSimTempScale; // enum to int
        float simtemp_high;
        float simtemp_low;

        bool bExpanded = false; // Whether expanded ensembles are used

        // em
        float   em_stepsize;
        float   em_tol;
        int64_t ld_seed = 0;

        // deform
        float deform[DIM * DIM] = {0};
        float cos_accel         = 0;
        int   userint1, userint2, userint3, userint4;
        float userreal1, userreal2, userreal3, userreal4;


        int ngacc  = 0; // ���������
        int ngfrz  = 0; // ���������
        int ngener = 0; // ���������

        // ���²��֣�ά��ngtc
        int                ngtc          = 0; // ��������Ŀ
        int                nhchainlength = 1;
        std::vector<float> nrdf;           // ÿ�������ɶ�
        std::vector<float> ref_t;          // ÿ����ο��¶�
        std::vector<int>   annealing;      // ÿ����ģ���˻�����, enum to int
        std::vector<int>   anneal_npoints; // ÿ����ģ���˻����
        vecF2D             anneal_time;    // ÿ����ģ���˻�ʱ���
        vecF2D             anneal_temp;    // ÿ����ģ���˻��¶ȵ�
        std::vector<float> tau_t;          // ÿ����ģ���˻�ʱ�䳣��

        std::vector<std::array<int, DIM>>   nFreeze;      // ÿ��������������ʱ�򱻶��ᣬά��ngfrz
        std::vector<std::array<float, DIM>> acceleration; // ÿ��������������ʱ�򱻶��ᣬά��ngacc
        std::vector<int> egp_flags; // ������ÿ��֮���Exclusions/tables��ά��ngener*ngener

        // ֧���º;ɰ汾gmx�糡��������. DIM*4 ÿ��ά���ĸ�����E0, omega, t0, sigma
        //! ��ʹmdp��û���õ糡��tpr����Ȼ�е糡���ֿɶ�����ֵ����0
        std::vector<float> elec_field;
        struct
        {
            int n = 0, nt = 0; // ʱ�䣬�ռ�������<=1
        } elec_old_gmx[DIM];   // �Ͱ汾tpr��
        //! �߰汾tpr�ã�
        int ncount      = 0; //< ����applied-forces��Ŀ������=1
        int napp_forces = 0; //< applied-forces�µ�����Ŀ��Ŀ
    } ir;


    struct
    {
        vecI2D           interactionlist[F_NRE];
        std::vector<int> nr[F_NRE];
    } ilist,                   ///< �����໥�����б�
        inter_molecular_ilist; ///< ȫ��ָ���ķ��Ӽ��໥����

    // ԭ������
    struct
    {
        std::vector<float>          x; ///< coordinates
        std::vector<float>          v; ///< velocity
        std::vector<float>          f; ///< force
        std::vector<std::string>    atomname;
        std::vector<std::string>    resname;
        std::vector<std::string>    atomtypename;   ///< atom type name from .ff
        std::vector<int>            atomtypenumber; ///< atomtype number, -1=unknown, 0=VSite
        std::vector<int>            resid;
        std::vector<float>          mass;
        std::vector<float>          charge;
        std::vector<int>            atomnumber; ///< atomic number, -1=unknown, 0=VSite
        std::vector<unsigned short> type;       ///< unused ?
        vecI2D excls; ///< atom exclusions inedx (0-based, is global index in system) list for each atom
    } atoms;

    //! �˴�û�н���ȥ�ظ���һ���ǿ��Դ��ڶ������
    // bonds (1-based)
    std::vector<Bonded> bonds;
    // angles (1-based)
    std::vector<Bonded> angles;
    // proper dihedrals (1-based)
    std::vector<Bonded> dihedrals;
    // improper dihedrals (1-based)
    std::vector<Bonded> impropers;
    // pairs/LJ_14
    std::vector<NonBonded> pairs;
    // only the atomtype LJ parameters
    std::vector<NonBonded> atomtypesLJ;
    // all atoms LJ parameters
    std::vector<NonBonded> ljparams;

    // mdp����λ��, ���б����������ʼ��Ϊ0
    struct
    {
        long nsteps = 0; //< the started nsteps position in tpr
        long dt     = 0; //< the started dt position in tpr
        long x      = 0; //< the started atom coordinates position in tpr
        long v      = 0; //< the started atom velocity position in tpr
        long f      = 0; //< the started atom force position in tpr
        long box    = 0; //< the box position in tpr
        long ef     = 0; //< the electric field started position in tpr


        // ѹ�����ò���λ��
        struct
        {
            long box_rel = 0; //< the started vector position for preserve box shape, is DIM*DIM vector
            long epc      = 0; //< the started pressure coupling method position
            long epct     = 0; //< the started pressure coupling type position
            long tau_p    = 0; //< the started tau_p position
            long ref_p    = 0; //< the started ref pressure value position, is DIM*DIM vector
            long compress = 0; //< the started compressibility value position, is DIM*DIM vector
            long deform   = 0; //< the started deform value positon, is DIM*DIM vector

            //< return False if get all parameters
            bool empty() const
            {
                return !(box_rel && epc && epct && tau_p && ref_p && compress && deform);
            }
        } press;

        // �¶����ò���λ��
        struct
        {
            long g_ngtc =
                0; //< the started number of temperature coupling group position in tpr header, g_ngtc==ir->ngtc
            long etc = 0; //< the started temperature coupling type position, enum to int, 0=No, 1=Berendsen,2=NoseHoover,6=VRescale
            long ngtc = 0;          //< the started number of temperature coupling group position
            long nhchainlength = 0; //< the Nose-Hoover chain length if use Nose-Hoover temperature coupling
            long ref_t = 0;         //< the started ref temperature position, is ir->ngtc vector
            long tau_t = 0; //< the started temperature coupling constant position, is ir->ngtc vector

            //< return True if can not read temperature position due to pull code, AWH have not yet finish in tpr reader (TODO)
            bool empty() const { return !(ref_t && tau_t && etc && ngtc && g_ngtc); }
        } temperature;

        // ������������mdp����λ��
        struct
        {
            //! �������˳������ͱ����ö��˳����ȫһ��
            long nstlog             = 0; // started
            long nstxout            = 0;
            long nstvout            = 0;
            long nstfout            = 0;
            long nstenergy          = 0;
            long nstxout_compressed = 0;

            // must be data_->filever >= 71
            long nsttcouple = 0;
            long nstpcouple = 0;

            // must be data_->filever >= 67
            long nstcalcenergy = 0;

            long nstlist = 0;
            long nstcomm = 0;

            //< return True if can not read any one position
            bool empty() const
            {
                return !(nstlog && nstxout && nstvout && nstfout && nstenergy && nstxout_compressed
                         && nsttcouple && nstpcouple && nstcalcenergy && nstlist && nstcomm);
            }
        } integer;

    } property;
};


//! Pull code data, from pull_params.h
/*! \brief Struct that defines a pull group */
struct t_pull_group
{
    std::vector<int>   ind;     /**< The global atoms numbers */
    std::vector<float> weight;  /**< Weights (use all 1 when weight==NULL) */
    int                pbcatom; /**< The reference atom for pbc (global number) */
    int pbcatom_input; /**< The reference atom for pbc (global number) as specified in the input parameters */
};

/*! Maximum number of pull groups that can be used in a pull coordinate */
static constexpr int c_pullCoordNgroupMax = 6;

/*! \brief Struct that defines a pull coordinate */
struct t_pull_coord
{
    //! The pull type: umbrella, constraint, ...
    PullingAlgorithm eType = PullingAlgorithm::Umbrella;
    //! Name of the module providing   the external potential, only used with eType==epullEXTERNAL
    std::string externalPotentialProvider;
    //! The pull geometry
    PullGroupGeometry eGeom = PullGroupGeometry::Distance;
    //! Mathematical expression evaluated by the pull code for transformation coordinates.
    std::string expression;
    //! The finite difference to use in numerical derivation of mathematical expressions
    double dx = 1e-9;
    //! The number of groups, depends on eGeom
    int ngroup = 0;
    /*! \brief The pull groups:
     *
     *  indices into the group arrays in pull_t and pull_params_t,
     *   ngroup indices are used
     */
    std::array<int, c_pullCoordNgroupMax> group;
    //! Used to select components for constraint
    int dim[DIM] = {0, 0, 0};
    //! The origin for the absolute reference
    float origin[DIM] = {0, 0, 0};
    //! The pull vector, direction or position
    float vec[DIM] = {0, 0, 0};
    //! Set init based on the initial structure
    bool bStart = false;
    //! Initial reference displacement (nm) or (deg)
    float init = 0.0;
    //! Rate of motion (nm/ps) or (deg/ps)
    float rate = 0.0;
    /*! \brief Force constant
     *
     * For umbrella pull type this is (kJ/(mol nm^2) or kJ/(mol rad^2).
     * For constant force pull type it is kJ/(mol nm) or kJ/(mol rad).
     */
    float k = 0.0;
    //! Force constant for state B
    float kB = 0.0;
    //! The index of this coordinate in the list of coordinates
    int coordIndex = -1;
};

struct PullData
{
    int   ngroup  = 0;
    int   ncoord  = 0;
    int   nstxout = 0;
    int   nstfout = 0;
    float cylinder_r, constr_tol;
    bool  bPrintCOM;
    bool  bPrintRefValue;
    bool  bPrintComp;
    bool  bSetPbcRefToPrevStepCOM;
    bool  bXOutAverage;
    bool  bFOutAverage;

    std::vector<t_pull_group> group;
    std::vector<t_pull_coord> coord;
};

struct t_rot
{
    //! Rot data
    struct t_rotgrp
    {
        //! Rotation type for this group
        EnforcedRotationGroupType eType = EnforcedRotationGroupType::Default;
        //! Use mass-weighed positions?
        bool bMassW = false;
        //! Number of atoms in the group
        int nat = 0;
        //! The global atoms numbers
        std::vector<int> ind;
        //! The reference positions (which have not been centered)
        std::vector<std::array<float, DIM>> x_ref_original;
        //! The normalized rotation vector
        float inputVec[DIM] = {0, 0, 0};
        //! Rate of rotation (degree/ps)
        float rate = 0;
        //! Force constant (kJ/(mol nm^2)
        float k = 0;
        //! Pivot point of rotation axis (nm)
        float pivot[DIM] = {0, 0, 0};
        //! Type of fit to determine actual group angle
        RotationGroupFitting eFittype = RotationGroupFitting::Default;
        //! Number of angles around the reference angle for which the rotation potential is also evaluated (for fit type 'potential' only)
        int PotAngle_nstep = 0;
        //! Distance between two angles in degrees (for fit type 'potential' only)
        float PotAngle_step = 0;
        //! Slab distance (nm)
        float slab_dist = 0;
        //! Minimum value the gaussian must have so that the force is actually evaluated
        float min_gaussian = 0;
        //! Additive constant for radial motion2 and flexible2 potentials (nm^2)
        float eps = 0;
    };


    //! Output frequency for main rotation outfile
    int nstrout;
    //! Output frequency for per-slab data
    int nstsout;
    //! Groups to rotate
    std::vector<t_rotgrp> grp;
};

#endif // !TPRDATA_H
