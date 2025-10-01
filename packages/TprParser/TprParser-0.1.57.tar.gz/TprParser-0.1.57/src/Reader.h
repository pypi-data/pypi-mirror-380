#ifndef READER_H
#define READER_H

#include <cstdint>
#include <cstring>
#include <memory> // unique_ptr

#include "define.h"
#include "FileSerializer.h"
#include "TprData.h"
#include "TprException.h"

#define INSERT_POS(prop) data_->property.prop = static_cast<long>(tpr_.ftell_())

class TprReader
{
public:
    const char* fout_ = nullptr;

public:
    TprReader(const char* fname, bool bGRO = false, bool bMol2 = false, bool bCharge = false);

    ~TprReader() { msg("End of TprReader\n"); }

    // read header
    bool tpr_header();

    // read body of tpr
    bool tpr_body();

    // read mtop
    bool tpr_mtop();

    //< read coodinates, velocity and force of atoms
    bool tpr_xvf();

    //< dump charges and mass
    bool tpr_chargemass();

    //< dump bonds of tpr, can store angle and harmonic force constant
    bool tpr_bonds();

    //< dump angles of tpr, can store angle and harmonic force constant
    bool tpr_angles();

    /*  \brief dump ALL dihedrals of tpr, can store dihedrals parameters
     */
    bool tpr_dihedrals();

    //< dump non-bonded parameters, includes LJ and paris
    bool tpr_nonbonded();

    /*< do_ir, have not yet completely completed
     * Unfinished:
     *	- AWH, ComputationalElectrophysiology, etc.
     */
    bool do_ir();

public:
    //< change tpr file nsteps
    bool set_nsteps(int64_t nsteps);

    //< change tpr file dt (ps)
    bool set_dt(double dt);

    //< change tpr vector property
    bool set_xvf(const char* type, std::vector<float>& vec);

    //< set pressure coupling parts, includes deform
    bool set_pressure(const char*         method,
                      const char*         type,
                      float               tau_p,
                      std::vector<float>& ref_p,
                      std::vector<float>& compress,
                      std::vector<float>& deform);

    //< set temperature coupling parts. Have not yet set groups name
    bool set_temperature(const char* method, std::vector<float>& tau_t, std::vector<float>& ref_t);

    //< set integer mdp parameters
    bool set_mdp_integer(const char* prop, int val);

    //< 1. get coords/velocity/force/mass/charge
    //< 2. get box info in vector 9
    //< 3. get electric field in vector DIM * 4 = 12
    const std::vector<float>& get_xvf(const char* type) const;

    //< get int vector, such resid, atomtypenumber, atomnumber...
    const std::vector<int>& get_ivector(const char* type) const;

    //< get resname, atomname
    const std::vector<std::string>& get_name(const char* type) const;

    //< get bonds/angles/dihedrals/impropers info in struct
    const std::vector<Bonded>& get_bonded(const char* type) const;

    //< get non-bonded pairs/LJ parameters
    const std::vector<NonBonded>& get_nonbonded(const char* type) const;

    //< get precision of tpr
    int get_precision() const { return data_->prec; }

    //< get integer mdp parameters
    int get_mdp_integer(const char* prop) const;

    //< get global exclusions list (0-based) for each atom
    const auto& get_exclusions() const { return data_->atoms.excls; }

    //< get electric field parts, throw error if can not find electric field
    const std::vector<float>& get_ef() const;

private:
    //< assistant func to write tpr given new coords, velocity or force
    bool write_xvf(std::vector<float>& vec, long pos, long prec) const;

    //< assistant func to write electric field to tpr
    bool write_ef(std::vector<float>& vec, long pos, long prec) const;

    //< read forcefield parameters
    bool tpr_readff();

    //< read parameters
    bool do_iparams(int ftype, t_iparams* iparams, int filever, int prec);

    //< moltype dump
    bool do_atoms();

    //< atomtype
    bool do_atomtypes();

    //< read cmap
    bool do_cmap();

    //< read groups
    bool do_groups();

    //< do_ilists
    bool do_ilists(int ntype, std::vector<int> (&nr)[F_NRE], vecI2D (&interactionlist)[F_NRE]);

    //< do_fepvals
    bool do_fepvals();

    //< do_pull
    bool do_pull(PullingAlgorithm ePullOld);
    //! internal function of do_pull
    bool do_pullgrp_tpx_pre95(t_pull_group* pgrp, t_pull_coord* pcrd);
    bool do_pull_group(t_pull_group* pgrp);
    bool do_pull_coord(t_pull_coord*     pcrd,
                       PullingAlgorithm  ePullOld,
                       PullGroupGeometry eGeomOld,
                       int               dimOld[DIM]);

    //< do_rot
    bool do_rot();

private:
    FileSerializer           tpr_;
    std::unique_ptr<TprData> data_;
    std::vector<t_iparams>   iparams_;         // ��������
    std::vector<int>         functype_;        // ��������
    bool                     bGRO_    = false; //< if write a gro
    bool                     bMol2_   = false; //< if write a mol2 whith bonds
    bool                     bCharge_ = false; //< if write atomic charge and mass to file
};

#endif // !READER_H
