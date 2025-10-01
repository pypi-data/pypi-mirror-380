#include "Utils.h"

#include <stdexcept>
#include <string>

#include "define.h"
#include "TprException.h"

std::pair<int, std::vector<float>> get_bond_type(int ftype, const t_iparams* param)
{
    std::vector<float> ffparam;
    switch (ftype)
    {
        case F_BONDS:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(1, ffparam);
        case F_G96BONDS:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(2, ffparam);
        case F_MORSE:
            ffparam.push_back(param->morse.b0A);
            ffparam.push_back(param->morse.cbA);
            ffparam.push_back(param->morse.betaA);
            ffparam.push_back(param->morse.b0B);
            ffparam.push_back(param->morse.cbB);
            ffparam.push_back(param->morse.betaB);
            return std::make_pair(3, ffparam);
        case F_CUBICBONDS:
            ffparam.push_back(param->cubic.b0);
            ffparam.push_back(param->cubic.kb);
            ffparam.push_back(param->cubic.kcub);
            return std::make_pair(4, ffparam);
        case F_CONNBONDS: return std::make_pair(5, ffparam);
        case F_HARMONIC:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(6, ffparam);
        case F_FENEBONDS:
            ffparam.push_back(param->fene.bm);
            ffparam.push_back(param->fene.kb);
            return std::make_pair(7, ffparam);
        case F_TABBONDS:
            ffparam.push_back(param->tab.kA);
            ffparam.push_back(static_cast<float>(param->tab.table)); // int to float
            ffparam.push_back(param->tab.kB);
            return std::make_pair(8, ffparam);
        case F_TABBONDSNC:
            ffparam.push_back(param->tab.kA);
            ffparam.push_back(static_cast<float>(param->tab.table)); // int to float
            ffparam.push_back(param->tab.kB);
            return std::make_pair(9, ffparam);
        case F_RESTRBONDS:
            ffparam.push_back(param->restraint.lowA);
            ffparam.push_back(param->restraint.up1A);
            ffparam.push_back(param->restraint.up2A);
            ffparam.push_back(param->restraint.kA);
            ffparam.push_back(param->restraint.lowB);
            ffparam.push_back(param->restraint.up1B);
            ffparam.push_back(param->restraint.up2B);
            ffparam.push_back(param->restraint.kB);
            return std::make_pair(10, ffparam);
        // add settle for water
        case F_SETTLE:
            ffparam.push_back(param->settle.doh);
            ffparam.push_back(param->settle.dhh);
            return std::make_pair(1, ffparam);
        // 1. ����[ constraints ]�Ĳ���
        // 2. ��Щ�ɼ���ϵ��ת����Լ��Constraint��ȡ����mdpԼ�����ã�����h-bonds
        case F_CONSTR:
            ffparam.push_back(param->constr.dA); // ����
            ffparam.push_back(param->constr.dB);
            return std::make_pair(1, ffparam);
        case F_CONSTRNC:
            ffparam.push_back(param->constr.dA); // ����
            ffparam.push_back(param->constr.dB);
            return std::make_pair(2, ffparam);
        default: break;
    }
    return std::make_pair(-1, ffparam);
}


std::pair<int, std::vector<float>> get_angle_type(int ftype, const t_iparams* param)
{
    std::vector<float> ffparam;
    switch (ftype)
    {
        case F_ANGLES:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(1, ffparam);
        case F_G96ANGLES:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(2, ffparam);
        case F_CROSS_BOND_BONDS:
            ffparam.push_back(param->cross_bb.r1e);
            ffparam.push_back(param->cross_bb.r2e);
            ffparam.push_back(param->cross_bb.krr);
            return std::make_pair(3, ffparam);
        case F_CROSS_BOND_ANGLES:
            ffparam.push_back(param->cross_ba.r1e);
            ffparam.push_back(param->cross_ba.r2e);
            ffparam.push_back(param->cross_ba.r3e);
            ffparam.push_back(param->cross_ba.krt);
            return std::make_pair(4, ffparam);
        case F_UREY_BRADLEY:
            ffparam.push_back(param->u_b.thetaA);
            ffparam.push_back(param->u_b.kthetaA);
            ffparam.push_back(param->u_b.r13A);
            ffparam.push_back(param->u_b.kUBA);
            ffparam.push_back(param->u_b.thetaB);
            ffparam.push_back(param->u_b.kthetaB);
            ffparam.push_back(param->u_b.r13B);
            ffparam.push_back(param->u_b.kUBB);
            return std::make_pair(5, ffparam);
        case F_QUARTIC_ANGLES:
            ffparam.push_back(param->qangle.theta);
            for (int i = 0; i < 5; i++)
                ffparam.push_back(param->qangle.c[i]);
            return std::make_pair(6, ffparam);
        case F_TABANGLES:
            ffparam.push_back(param->tab.kA);
            ffparam.push_back(static_cast<float>(param->tab.table)); // int to float
            ffparam.push_back(param->tab.kB);
            return std::make_pair(8, ffparam);
        case F_LINEAR_ANGLES: // the order is different from tpr
            ffparam.push_back(param->linangle.aA);
            ffparam.push_back(param->linangle.klinA);
            ffparam.push_back(param->linangle.aB);
            ffparam.push_back(param->linangle.klinB);
            return std::make_pair(9, ffparam);
        case F_RESTRANGLES:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            return std::make_pair(10, ffparam);
        default: break;
    }

    return std::make_pair(-1, ffparam);
}

std::pair<int, std::vector<float>> get_dihedral_type(int ftype, const t_iparams* param)
{
    std::vector<float> ffparam;
    switch (ftype)
    {
        case F_PDIHS: // �����Զ���Ƕ���
            ffparam.push_back(param->pdihs.phiA);
            ffparam.push_back(param->pdihs.cpA);
            ffparam.push_back(param->pdihs.phiB);
            ffparam.push_back(param->pdihs.cpB);
            ffparam.push_back(static_cast<float>(param->pdihs.mult));
            // return 1;
            return std::make_pair(9, ffparam);
        case F_RBDIHS:
            for (int i = 0; i < 6; i++)
                ffparam.push_back(param->rbdihs.rbcA[i]);
            for (int i = 0; i < 6; i++)
                ffparam.push_back(param->rbdihs.rbcB[i]);
            return std::make_pair(3, ffparam);
        case F_FOURDIHS:
            for (int i = 0; i < 6; i++)
                ffparam.push_back(param->rbdihs.rbcA[i]);
            for (int i = 0; i < 6; i++)
                ffparam.push_back(param->rbdihs.rbcB[i]);
            return std::make_pair(5, ffparam);
        case F_TABDIHS:
            ffparam.push_back(param->tab.kA);
            ffparam.push_back(static_cast<float>(param->tab.table)); // int to float
            ffparam.push_back(param->tab.kB);
            return std::make_pair(8, ffparam);
        case F_RESTRDIHS:
            ffparam.push_back(param->pdihs.phiA);
            ffparam.push_back(param->pdihs.cpA);
            return std::make_pair(10, ffparam);
        case F_CBTDIHS:
            for (int i = 0; i < 6; i++)
                ffparam.push_back(param->cbtdihs.cbtcA[i]);
            return std::make_pair(11, ffparam);
        default: break;
    }
    return std::make_pair(-1, ffparam);
}

std::pair<int, std::vector<float>> get_improper_type(int ftype, const t_iparams* param)
{
    std::vector<float> ffparam;
    switch (ftype)
    {
        case F_IDIHS:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(2, ffparam);
        case F_PIDIHS:
            ffparam.push_back(param->harmonic.rA);
            ffparam.push_back(param->harmonic.krA);
            ffparam.push_back(param->harmonic.rB);
            ffparam.push_back(param->harmonic.krB);
            return std::make_pair(4, ffparam);
        default: break;
    }
    return std::make_pair(-1, ffparam);
}

std::pair<int, std::vector<float>> get_nonbonded_type(int ftype, const t_iparams* param)
{
    std::vector<float> ffparam;

    switch (ftype)
    {
        case F_LJ: // I set up functyepe=3
            ffparam.push_back(param->lj.c6);
            ffparam.push_back(param->lj.c12);
            return std::make_pair(3, ffparam);
        case F_LJ14: // [ pairs ], functype 1
            ffparam.push_back(param->lj14.c6A);
            ffparam.push_back(param->lj14.c12A);
            ffparam.push_back(param->lj14.c6B);
            ffparam.push_back(param->lj14.c12B);
            return std::make_pair(1, ffparam);
        default: break;
    }
    return std::make_pair(-1, ffparam);
}

FILE* efopen(const char* fname, const char* mod)
{
    FILE* fp = fopen(fname, mod);
    if (!fp) { THROW_TPR_EXCEPTION(std::string("Can not open/write file: ") + fname); }
    return fp;
}


//! TODO:
class KeyValueTreeObj
{
public:
};

class KeyValueTreeArray
{
public:
};


class AppliedForces;

struct Serializer
{
    unsigned char typeTag;
    //! ʵ�ʽ����л�����ָ��
    std::function<void(AppliedForces*)> deserialize;
};

//! macro to simplify the definition of serializer
#define SERIALIZER(tag, type)                     \
    {                                             \
        std::type_index(typeid(type)),            \
        {                                         \
            tag, &Deserializer<type>::deserialize \
        }                                         \
    }


template<typename T>
struct Deserializer;

template<>
struct Deserializer<KeyValueTreeObj>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<KeyValueTreeArray>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<std::string>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<bool>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<char>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<unsigned char>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<int>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<int64_t>
{
    static void deserialize(AppliedForces* obj);
};

template<>
struct Deserializer<float>
{
    static void deserialize(AppliedForces* obj);
};


template<>
struct Deserializer<double>
{
    static void deserialize(AppliedForces* obj);
};

static const std::map<std::type_index, Serializer> s_serializers = {
    SERIALIZER('O', KeyValueTreeObj),
    SERIALIZER('A', KeyValueTreeArray),
    SERIALIZER('s', std::string),
    SERIALIZER('b', bool),
    SERIALIZER('c', char),
    SERIALIZER('u', unsigned char),
    SERIALIZER('i', int),
    SERIALIZER('l', int64_t),
    SERIALIZER('f', float),
    SERIALIZER('d', double),
};


AppliedForces::AppliedForces(const FileSerializer& tpr, std::unique_ptr<TprData>& data)
    : tpr_(tpr), data_(data), m_name(""), m_typeTag('\0')
{
    //! typeTag -> deserialize function
    for (const auto& it : s_serializers)
    {
        s_deserializers[it.second.typeTag] = it.second.deserialize;
    }
}

bool AppliedForces::deserialize()
{
    if (!tpr_.do_int(&data_->ir.ncount)) return TPR_FAILED;
    msg("nf count= %d\n", data_->ir.ncount);
    if (data_->ir.ncount != 1)
    {
        THROW_TPR_EXCEPTION("Something is wrong in AppliedForces, ir.ncount must be 1");
    }

    char          tempstr[MAX_LEN];
    unsigned char typeTag;
    //! 'applied-forces' item
    if (!tpr_.do_string(tempstr, data_->vergen)) return TPR_FAILED;
    if (!tpr_.do_uchar(&typeTag, data_->vergen)) return TPR_FAILED;
    msg("name= '%s'\n", tempstr);    ///< ��Ŀ���ƣ�����'applied-forces'�ַ���
    msg("typeTag= '%c'\n", typeTag); // �����л����ͣ�����'O'��ʾobj
    auto it = s_deserializers.find(typeTag);
    if (it == s_deserializers.end())
    {
        THROW_TPR_EXCEPTION("Unknown type tag for deserializization: " + typeTag);
    }
    it->second(this);

    return TPR_SUCCESS;
}


//! ʵ��
void Deserializer<KeyValueTreeObj>::deserialize(AppliedForces* obj)
{
    int           count;
    char          tempstr[MAX_LEN];
    unsigned char typeTag;
    obj->tpr_.do_int(&count);
    msg("countXXX= %d\n", count);
    for (int i = 0; i < count; i++)
    {
        obj->tpr_.do_string(tempstr, obj->data_->vergen);
        obj->tpr_.do_uchar(&typeTag, obj->data_->vergen);
        msg("tempstrXXX= %s\n", tempstr);
        msg("typeTagXXX= %c\n", typeTag);

        //! save it
        obj->m_name    = tempstr;
        obj->m_typeTag = typeTag;

        //! save applied-forces�µ�����Ŀ��
        if (obj->m_name == "electric-field")
        {
            obj->data_->ir.napp_forces = count;
            msg("ne count= %d\n", obj->data_->ir.napp_forces);
        }

        auto it = obj->s_deserializers.find(typeTag);
        if (it == obj->s_deserializers.end())
        {
            THROW_TPR_EXCEPTION("Unknown type tag for deserializization: " + typeTag);
        }
        it->second(obj);
    }
}


void Deserializer<KeyValueTreeArray>::deserialize(AppliedForces* obj)
{
    THROW_TPR_EXCEPTION("Have not support deserialize KeyValueTreeArray");
}

void Deserializer<std::string>::deserialize(AppliedForces* obj)
{
    char val[MAX_LEN];
    obj->tpr_.do_string(val, obj->data_->vergen);
    msg("valstring= %s\n", val);
}

void Deserializer<bool>::deserialize(AppliedForces* obj)
{
    bool val;
    obj->tpr_.do_bool(&val, obj->data_->vergen);
    msg("valbool= %s\n", val ? "True" : "Flase");
}

void Deserializer<char>::deserialize(AppliedForces* obj)
{
    unsigned char val;
    obj->tpr_.do_uchar(&val);
    msg("valchar= %c\n", val);
}


void Deserializer<unsigned char>::deserialize(AppliedForces* obj)
{
    unsigned char val;
    obj->tpr_.do_uchar(&val);
    msg("valuchar= %c\n", val);
}

void Deserializer<int>::deserialize(AppliedForces* obj)
{
    int val;
    obj->tpr_.do_int(&val);
    msg("valint= %d\n", val);
}

void Deserializer<int64_t>::deserialize(AppliedForces* obj)
{
    int64_t val;
    obj->tpr_.do_int64(&val);
    msg("valint64= %lld\n", val);
}

void Deserializer<float>::deserialize(AppliedForces* obj)
{
    float val;
    obj->tpr_.do_float(&val);
    msg("valfloat= %f\n", val);

    //! add float value
    obj->m_efield[obj->m_name].push_back(val);
}

void Deserializer<double>::deserialize(AppliedForces* obj)
{
    double val;
    obj->tpr_.do_double(&val);
    msg("valdouble= %f\n", val);
}
