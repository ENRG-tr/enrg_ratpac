// Author: Ayse Bat <aysebat@erciyes.edu.tr>
#include <RAT/EnrgDetectorFactory.hh>
#include <RAT/Log.hh>
#include <RAT/DB.hh>

#include <cmath>
#include <vector>

using namespace std;

using namespace RAT {
	void EnrgDetectorFactory::DefineDetector(DBLinkPtr /*detector*/) {
		const std::string geo_template = "enrg/enrg_3t.geo"
		DB *db = DB::Get();
		if (db->Load(geo_template) == 0) {
			Log::Die("EnrgDetectorFactory: could not load template enrg/enrg.geo");
		}

		 DBLinkPtr inner_pmts = db->GetLink("GEO","inner_pmts");

		  db->SetI("GEO","inner_pmts","start_idx",0);
                  db->SetI("GEO","inner_pmts","end_idx",num_pmts-1);
	}
}


