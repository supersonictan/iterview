#include <iostream>
#include <vector>

using namespace std;

int main() {
    std::cout << "Hello, World!" << std::endl;


    vector<vector<uint32_t>> aliasTermsVec_seg1;
    vector<vector<uint32_t>> aliasWeightsVec_seg1;

    vector<uint32_t> aliasTermsTotal;
    aliasTermsTotal.push_back(2);
    aliasTermsTotal.push_back(194180932);
    aliasTermsTotal.push_back(134567);
    aliasTermsTotal.push_back(3302234209);
    aliasTermsTotal.push_back(47620);
    aliasTermsTotal.push_back(3);
    aliasTermsTotal.push_back(194180932);
    aliasTermsTotal.push_back(134567);
    aliasTermsTotal.push_back(3585031579);
    aliasTermsTotal.push_back(116584);
    aliasTermsTotal.push_back(1929370669);
    aliasTermsTotal.push_back(27868);


    vector<uint32_t>* tmpTermVec; //当前show的term vector
    vector<uint32_t>* tmpWeightVec; //当前show的weight vector
    uint32_t remainTerms = 0;
    //2 194180932 134567 3302234209 47620 3 194180932 134567 3585031579 116584 1929370669 27868 2 2044737783 30354 194180932 134567 5 2068004672 53837 3370521906 36000 818911323 56218 3370521906 36000 2515168961 43056
    for(size_t i=0; i<aliasTermsTotal.size(); ++i) {
        if (remainTerms == 0) {
            if (i != 0) {
                aliasTermsVec_seg1.push_back(*tmpTermVec);
                aliasWeightsVec_seg1.push_back(*tmpWeightVec);
            }
            remainTerms = aliasTermsTotal[i] * 2; //terms和权重
            vector<uint32_t> tmp;
            vector<uint32_t> tmp_w;
            tmpTermVec = &tmp;
            tmpWeightVec = &tmp_w;


            continue;
        }
        if (remainTerms%2 == 0) { //term值
            uint32_t termId = aliasTermsTotal[i];
            (*tmpTermVec).push_back(termId);
        } else { //weight value
            uint32_t weight = aliasTermsTotal[i];
            (*tmpWeightVec).push_back(weight);
        }
        remainTerms -= 1;
        if (i == (aliasTermsTotal.size()-1) ){
            aliasTermsVec_seg1.push_back(*tmpTermVec);
            aliasWeightsVec_seg1.push_back(*tmpWeightVec);
        }
    }
    cout<<aliasTermsVec_seg1[0][0]<<endl;
    cout<<aliasTermsVec_seg1[1][1]<<endl;




    /*std::vector<int32_t >* v;
    std::vector<vector<int32_t>> vec;

    for (int i = 0; i < 5; ++i) {
        std::vector<int32_t> tmpVec;
        //tmpVec.push_back(i);
        v = &tmpVec;
        (*v).push_back(i);
        vec.push_back(*v);
    }
    cout<< vec[0][0]<<endl;
    cout<< vec[1][0]<<endl;
    cout<< vec[2][0]<<endl;
    cout<< vec[3][0]<<endl;
    cout<< vec[4][0]<<endl;
    cout << vec.size()<<endl;*/

    return 0;
}