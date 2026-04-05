%define		packname	Gviz

%undefine	_debugsource_packages
Summary:	Plotting data and annotation information along genomic coordinates
Name:		R-%{packname}
Version:	1.54.0
Release:	1
License:	Artistic 2.0
Group:		X11/Applications
Source0:	https://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	cd0fa7b7ace17f2d8343b3caba113207
URL:		https://bioconductor.org/packages/release/bioc/html/Gviz.html
BuildRequires:	R
BuildRequires:	R-biovizBase
BuildRequires:	R-cran-latticeExtra
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-biovizBase
Requires:	R-cran-latticeExtra
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genomic data analyses requires integrated visualization of known
genomic information and new experimental data. Gviz uses the biomaRt
and the rtracklayer packages to perform live annotation queries to
Ensembl and UCSC and translates this to e.g. gene/transcript
structures in viewports of the grid graphics package. This results in
genomic information plotted together with your data.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/data/
%{_libdir}/R/library/%{packname}/extdata/
%{_libdir}/R/library/%{packname}/lib/
%{_libdir}/R/library/%{packname}/scripts/
