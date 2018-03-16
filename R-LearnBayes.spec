#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-LearnBayes
Version  : 2.15
Release  : 1
URL      : https://cran.r-project.org/src/contrib/LearnBayes_2.15.tar.gz
Source0  : https://cran.r-project.org/src/contrib/LearnBayes_2.15.tar.gz
Summary  : Functions for Learning Bayesian Inference
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n LearnBayes

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521209581

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521209581
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library LearnBayes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library LearnBayes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library LearnBayes
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library LearnBayes|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/LearnBayes/DESCRIPTION
/usr/lib64/R/library/LearnBayes/INDEX
/usr/lib64/R/library/LearnBayes/Meta/Rd.rds
/usr/lib64/R/library/LearnBayes/Meta/data.rds
/usr/lib64/R/library/LearnBayes/Meta/demo.rds
/usr/lib64/R/library/LearnBayes/Meta/features.rds
/usr/lib64/R/library/LearnBayes/Meta/hsearch.rds
/usr/lib64/R/library/LearnBayes/Meta/links.rds
/usr/lib64/R/library/LearnBayes/Meta/nsInfo.rds
/usr/lib64/R/library/LearnBayes/Meta/package.rds
/usr/lib64/R/library/LearnBayes/Meta/vignette.rds
/usr/lib64/R/library/LearnBayes/NAMESPACE
/usr/lib64/R/library/LearnBayes/R/LearnBayes
/usr/lib64/R/library/LearnBayes/R/LearnBayes.rdb
/usr/lib64/R/library/LearnBayes/R/LearnBayes.rdx
/usr/lib64/R/library/LearnBayes/data/Rdata.rdb
/usr/lib64/R/library/LearnBayes/data/Rdata.rds
/usr/lib64/R/library/LearnBayes/data/Rdata.rdx
/usr/lib64/R/library/LearnBayes/demo/Chapter.1.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.1.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.10.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.10.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.10.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.2.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.2.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.2.5.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.2.6.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.3.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.3.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.3.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.3.5.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.3.6.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.4.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.4.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.4.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.4.5.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.5.10.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.5.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.5.6.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.5.7.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.5.8.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.5.9.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.6.10.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.6.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.6.7.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.6.8.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.6.9.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.10.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.5.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.7.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.8.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.7.9.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.8.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.8.4.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.8.6.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.8.7.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.8.8.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.9.2.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.9.3.R
/usr/lib64/R/library/LearnBayes/demo/Chapter.9.4.R
/usr/lib64/R/library/LearnBayes/doc/BayesFactors.R
/usr/lib64/R/library/LearnBayes/doc/BayesFactors.Rnw
/usr/lib64/R/library/LearnBayes/doc/BayesFactors.pdf
/usr/lib64/R/library/LearnBayes/doc/BinomialInference.R
/usr/lib64/R/library/LearnBayes/doc/BinomialInference.Rnw
/usr/lib64/R/library/LearnBayes/doc/BinomialInference.pdf
/usr/lib64/R/library/LearnBayes/doc/DiscreteBayes.R
/usr/lib64/R/library/LearnBayes/doc/DiscreteBayes.Rnw
/usr/lib64/R/library/LearnBayes/doc/DiscreteBayes.pdf
/usr/lib64/R/library/LearnBayes/doc/MCMCintro.R
/usr/lib64/R/library/LearnBayes/doc/MCMCintro.Rnw
/usr/lib64/R/library/LearnBayes/doc/MCMCintro.pdf
/usr/lib64/R/library/LearnBayes/doc/MultilevelModeling.R
/usr/lib64/R/library/LearnBayes/doc/MultilevelModeling.Rnw
/usr/lib64/R/library/LearnBayes/doc/MultilevelModeling.pdf
/usr/lib64/R/library/LearnBayes/doc/index.html
/usr/lib64/R/library/LearnBayes/help/AnIndex
/usr/lib64/R/library/LearnBayes/help/LearnBayes.rdb
/usr/lib64/R/library/LearnBayes/help/LearnBayes.rdx
/usr/lib64/R/library/LearnBayes/help/aliases.rds
/usr/lib64/R/library/LearnBayes/help/paths.rds
/usr/lib64/R/library/LearnBayes/html/00Index.html
/usr/lib64/R/library/LearnBayes/html/R.css
