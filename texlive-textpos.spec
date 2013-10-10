# revision 28261
# category Package
# catalog-ctan /macros/latex/contrib/textpos
# catalog-date 2012-06-01 19:23:46 +0200
# catalog-license gpl
# catalog-version 1.7h
Name:		texlive-textpos
Version:	1.7h
Release:	1
Summary:	Place boxes at arbitrary positions on the LaTeX page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textpos
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpos.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpos.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to facilitate placement of boxes at absolute
positions on the LaTeX page. There are several reasons why this
might be useful, an important one being to help the creation of
large-format conference posters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textpos/textpos.sty
%doc %{_texmfdistdir}/doc/latex/textpos/LICENCE
%doc %{_texmfdistdir}/doc/latex/textpos/README
%doc %{_texmfdistdir}/doc/latex/textpos/VERSION-1.7i
%doc %{_texmfdistdir}/doc/latex/textpos/examples/README
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t1.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t2.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t3.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t4.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t5.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t6.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t7.tex
%doc %{_texmfdistdir}/doc/latex/textpos/examples/t8.tex
%doc %{_texmfdistdir}/doc/latex/textpos/niepraschk-eso-pic.pdf
%doc %{_texmfdistdir}/doc/latex/textpos/niepraschk-eso-pic.tex
%doc %{_texmfdistdir}/doc/latex/textpos/textpos-example.tex
%doc %{_texmfdistdir}/doc/latex/textpos/textpos.html
%doc %{_texmfdistdir}/doc/latex/textpos/textpos.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textpos/textpos.drv
%doc %{_texmfdistdir}/source/latex/textpos/textpos.dtx
%doc %{_texmfdistdir}/source/latex/textpos/textpos.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
