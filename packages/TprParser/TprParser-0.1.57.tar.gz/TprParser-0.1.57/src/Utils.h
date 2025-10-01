#ifndef UTILS_H
#define UTILS_H

#include <cstdio>
#include <functional>
#include <map>
#include <memory>
#include <string>
#include <typeindex>
#include <utility> // std::pair
#include <vector>

#include "define.h"
#include "FileSerializer.h"
#include "TprData.h"

/* \brief return bond function type id and force parameters.
 * includes constraint derived from bonds
 * \return return std::pair(-1, {}) if failed
 */
std::pair<int, std::vector<float>> get_bond_type(int ftype, const t_iparams* param);

/* \brief return angle function type id and force parameters,
 * \return return std::pair(-1, {}) if failed
 */
std::pair<int, std::vector<float>> get_angle_type(int ftype, const t_iparams* param);

/* \brief return dihedral function type id and force parameters,
 * \return return std::pair(-1, {}) if failed
 */
std::pair<int, std::vector<float>> get_dihedral_type(int ftype, const t_iparams* param);

/* \brief return impropers dihedral function type id and force parameters,
 * \return return std::pair(-1, {}) if failed
 */
std::pair<int, std::vector<float>> get_improper_type(int ftype, const t_iparams* param);

/* \brief return nonbonded (LJ/LJ-14) function type id and force parameters,
 * ifunc=1 is LJ-14, ifunc=3 is LJ
 * \return return std::pair(-1, {}) if failed
 */
std::pair<int, std::vector<float>> get_nonbonded_type(int ftype, const t_iparams* param);

/* \brief safely fopen */
FILE* efopen(const char* fname, const char* mod);

/* \brief A class to read applied forces from tpr file */
class AppliedForces
{
public:
    AppliedForces(const FileSerializer& tpr, std::unique_ptr<TprData>& data);

    //! ִ��tpr�����л�����
    bool deserialize();

public:
    //! �����л��ֵ�
    std::map<unsigned char, std::function<void(AppliedForces*)>> s_deserializers;
    //! �ַ��� -> ��������
    std::map<std::string, std::vector<float>> m_efield;
    std::string                               m_name;    //! current string name
    unsigned char                             m_typeTag; //! current typeTag
    const FileSerializer&                     tpr_;      //! tpr reference
    std::unique_ptr<TprData>&                 data_;     //! TprData reference
};

#endif // !UTILS_H
