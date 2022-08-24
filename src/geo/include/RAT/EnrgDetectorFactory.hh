///////////////////////////////////////////////////////////////////////////////
/// \class RAT::EnrgDetectorFactory
///
/// \brief  Rebuilds the Enrg detector on the fly based on simple parameters
///         
/// \author Ayse Bat <aysebat@erciyes.edu.tr>
///
///
/// \details Uses the geometry template in enrg/enrg.geo but positions and 
///          resizes components on the fly according the parameters given in 
///          the table named Enrg_PARAMS. This DetectorFactory is registered as 
///          "Enrg" and is preferred to using the .geo file directly. 
///
///////////////////////////////////////////////////////////////////////////////

#ifndef __RAT_EnrgDetectorFactory__
#define __RAT_EnrgDetectorFactory__

#include <RAT/DetectorFactory.hh>

namespace RAT {

class EnrgDetectorFactory : public DetectorFactory {

    public:
        EnrgDetectorFactory() { }
        virtual ~EnrgDetectorFactory() { }
        
    protected:
        virtual void DefineDetector(DBLinkPtr detector);

};

} //namespace RAT

#endif
