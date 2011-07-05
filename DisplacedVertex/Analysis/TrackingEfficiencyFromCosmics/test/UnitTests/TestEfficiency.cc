#include <cppunit/TestFixture.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/TestResult.h>
#include <cppunit/TestRunner.h>
#include <cppunit/ui/text/TestRunner.h>
#include <cppunit/TestResultCollector.h>
#include <cppunit/TextTestProgressListener.h>
#include <cppunit/CompilerOutputter.h>

#include "Analysis/TrackingEfficiencyFromCosmics/interface/Efficiency.h"

#define protected public
#define private public
#include "Analysis/TrackingEfficiencyFromCosmics/interface/Efficiency.h"
#undef protected
#undef private

class TestEfficiency : public CppUnit::TestFixture
{
 public:
  TestEfficiency() {}

  void setUp()
  {
    vPars_.push_back(Efficiency::Parameters("par1", 20, 0, 10));
    vPars_.push_back(Efficiency::Parameters("par2", 10, -3, 3));
    vPars_.push_back(Efficiency::Parameters("par3", 10, -3.2, 3.2));
    vPars_.push_back(Efficiency::Parameters("par4", 30, 0, 100));
    eff.reset(new Efficiency(vPars_));

    variables.reset(new double[4]);
    binIndex.reset(new unsigned int[4]);
    vKeep.reset(new int[4]);
  }

  void tearDown() {}

  void testGetLinearIndex()
  {
    boost::shared_array<unsigned int> vIndexes(new unsigned int[vPars_.size()]);
    vIndexes[0] = 0;
    vIndexes[1] = 0;
    vIndexes[2] = 0;
    vIndexes[3] = 0;
    CPPUNIT_ASSERT( eff->getLinearIndex(vIndexes) == 0 );
    vIndexes[0] = 2;
    vIndexes[1] = 3;
    vIndexes[2] = 6;
    vIndexes[3] = 15;
    CPPUNIT_ASSERT( eff->getLinearIndex(vIndexes) == (15 + vPars_[3].bins*(6 + vPars_[2].bins*(3 + 2*vPars_[1].bins))) );
    vIndexes[0] = 19;
    vIndexes[1] = 9;
    vIndexes[2] = 9;
    vIndexes[3] = 29;
    CPPUNIT_ASSERT( eff->getLinearIndex(vIndexes) == (29 + vPars_[3].bins*(9 + vPars_[2].bins*(9 + 19*vPars_[1].bins))) );
  }

  void testLinearRepresentation()
  {
    CPPUNIT_ASSERT( eff->getLinearSize() == (vPars_[0].bins)*(vPars_[1].bins)*(vPars_[2].bins)*(vPars_[3].bins) );
  }

  void testParameters()
  {
    for( unsigned int i=0; i<vPars_.size(); ++i ) {
      CPPUNIT_ASSERT( eff->bins(i) == vPars_[i].bins );
      CPPUNIT_ASSERT( float(eff->binsSize(i)) == float((vPars_[i].max - vPars_[i].min)/vPars_[i].bins) );
      CPPUNIT_ASSERT( eff->min(i) == vPars_[i].min );
      CPPUNIT_ASSERT( eff->max(i) == vPars_[i].max );
    }
  }

  void testGetIndexes()
  {
    boost::shared_array<int> vKeep(new int[4]);
    vKeep[0] = 0;
    vKeep[1] = -1;
    vKeep[2] = -1;
    vKeep[3] = 0;

    boost::shared_array<unsigned int> indexArray(eff->getIndexes(0, vKeep, 2));
    CPPUNIT_ASSERT( indexArray[0] == 0 );
    CPPUNIT_ASSERT( indexArray[1] == 0 );
    indexArray = eff->getIndexes(5, vKeep, 2);
    CPPUNIT_ASSERT( indexArray[0] == 0 );
    CPPUNIT_ASSERT( indexArray[1] == 5 );

    boost::shared_array<unsigned int> vIndexes(new unsigned int[vPars_.size()]);
    vIndexes[0] = 2;
    vIndexes[1] = 3;
    vIndexes[2] = 6;
    vIndexes[3] = 15;
    indexArray = eff->getIndexes(eff->getLinearIndex(vIndexes), vKeep, 2);
    CPPUNIT_ASSERT( indexArray[0] == 2 );
    CPPUNIT_ASSERT( indexArray[1] == 15 );

    // Case of projection on a single variable
    vKeep[0] = -1;
    vKeep[1] = -1;
    vKeep[2] = 0;
    vKeep[3] = -1;
    indexArray = eff->getIndexes(eff->getLinearIndex(vIndexes), vKeep, 1);
    CPPUNIT_ASSERT( indexArray[0] == 6 );

    // Case of projection on another single variable
    vKeep[0] = -1;
    vKeep[1] = 0;
    vKeep[2] = -1;
    vKeep[3] = -1;
    indexArray = eff->getIndexes(eff->getLinearIndex(vIndexes), vKeep, 1);
    CPPUNIT_ASSERT( indexArray[0] == 3 );
  }

  void testFill()
  {
    variables[0] = 4.2;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, false);
    eff->fill(variables, true);

    fillBinIndex(variables, binIndex);
    CPPUNIT_ASSERT(float(eff->getEff(binIndex)) == float(0.5));

    // Test filling with the negative value, it will go in the first bin (if not protected it will go in a UINT_MAX number for the bin...)
    variables[0] = -40.;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, false);
    eff->fill(variables, true);

    fillBinIndex(variables, binIndex);
    CPPUNIT_ASSERT(float(eff->getEff(binIndex)) == float(0.5));
  }

  void testEfficiency()
  {
    variables[0] = 3.8;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, false);
    eff->fill(variables, false);
    eff->fill(variables, true);
    fillBinIndex(variables, binIndex);
    CPPUNIT_ASSERT( eff->getEff(binIndex) == 1./3. );

    // Change only the first variable, the other bins are the same
    variables[0] = 3.2;
    eff->fill(variables, true);
    eff->fill(variables, true);
    eff->fill(variables, true);
    fillBinIndex(variables, binIndex);
    CPPUNIT_ASSERT( eff->getEff(binIndex) == 1. );
  }

  void testEffError()
  {
    variables[0] = 3.8;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, false);
    eff->fill(variables, false);
    eff->fill(variables, true);
    eff->fill(variables, true);
    fillBinIndex(variables, binIndex);
    float error = sqrt(1./2.*(1. - 1./2.)/4.);
    CPPUNIT_ASSERT( float(eff->getEffError(binIndex)) == error );

    // Compute errors after a projection
    vKeep[0] = -1;
    vKeep[1] = 0;
    vKeep[2] = -1;
    vKeep[3] = -1;

    boost::shared_ptr<Efficiency> newEff(eff->project(vKeep));
    unsigned int bin = (0.3 - vPars_[1].min)*vPars_[1].bins/(vPars_[1].max - vPars_[1].min);
    CPPUNIT_ASSERT( float(newEff->getEffError(bin)) == error );
  }

  void testProjection()
  {
    // Project on a single variable
    vKeep[0] = 0;
    vKeep[1] = -1;
    vKeep[2] = -1;
    vKeep[3] = -1;

    variables[0] = 3.8;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, false);
    eff->fill(variables, false);
    eff->fill(variables, true);

    boost::shared_ptr<Efficiency> newEff(eff->project(vKeep));
    unsigned int bin = (3.8 - vPars_[0].min)*vPars_[0].bins/(vPars_[0].max - vPars_[0].min);
    // std::cout << "newSize = " << newEff->getLinearSize() << std::endl;
    // std::cout << "newEff("<<bin<<") = " << newEff->getEff(bin) << std::endl;
    CPPUNIT_ASSERT( newEff->getEff(bin) == 1./3. );
    CPPUNIT_ASSERT( newEff->getName(0) == "par1" );

    // Fill the values changing the first variable such that they go in three different bins.
    variables[0] = 4.2;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, false);
    variables[0] = 3.2;
    variables[1] = 0.3;
    variables[2] = 5.;
    variables[3] = 45.;
    eff->fill(variables, true);
    // Project on another variable, see that the values in the first variable (that are in three different bins)
    // are collapsed in the correct way.
    // Expected value for the efficiency is 2/5
    vKeep[0] = -1;
    vKeep[1] = 0;
    vKeep[2] = -1;
    vKeep[3] = -1;
    newEff = eff->project(vKeep);
    // bin = (0.3 - vPars_[1].min)*vPars_[1].bins/(vPars_[1].max - vPars_[1].min);
    double binSize = (vPars_[1].max - vPars_[1].min)/vPars_[1].bins;
    // std::cout << "binSize = " << binSize << std::endl;
    bin = (unsigned int)((0.3 - vPars_[1].min)/binSize);
    // std::cout << "newEff("<<bin<<") = " << newEff->getEff(bin) << std::endl;
    // for( unsigned int i=0; i<vPars_[1].bins; ++i ) {
    //   std::cout << "newEff("<<i<<") = " << newEff->getEff(i) << std::endl;
    // }
    CPPUNIT_ASSERT( newEff->getEff(bin) == 2./5. );
    CPPUNIT_ASSERT( newEff->getName(0) == "par2" );
  }

  void fillBinIndex( boost::shared_array<double> variables,
                     boost::shared_array<unsigned int> & binIndex )
  {
    for( unsigned int i=0; i<4; ++i ) {
      if( variables[i] < vPars_[i].min ) binIndex[i] = 0;
      else if( variables[i] >= vPars_[i].max ) binIndex[i] = vPars_[i].bins - 1;
      else binIndex[i] = (variables[i]-vPars_[i].min)*vPars_[i].bins/(vPars_[i].max - vPars_[i].min);
    }
  }

  CPPUNIT_TEST_SUITE( TestEfficiency );
  CPPUNIT_TEST( testLinearRepresentation );
  CPPUNIT_TEST( testParameters );
  CPPUNIT_TEST( testGetLinearIndex );
  CPPUNIT_TEST( testGetIndexes );
  CPPUNIT_TEST( testFill );
  CPPUNIT_TEST( testEfficiency );
  CPPUNIT_TEST( testEffError );
  CPPUNIT_TEST( testProjection );
  CPPUNIT_TEST_SUITE_END();

  std::auto_ptr<Efficiency> eff;
  std::vector<Efficiency::Parameters> vPars_;
  boost::shared_array<double> variables;
  boost::shared_array<unsigned int> binIndex;
  boost::shared_array<int> vKeep;
};

CPPUNIT_TEST_SUITE_REGISTRATION( TestEfficiency );
