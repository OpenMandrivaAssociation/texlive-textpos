Name:		texlive-textpos
Version:	1.8
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
%{_texmfdistdir}/tex/latex/textpos
%doc %{_texmfdistdir}/doc/latex/textpos
#- source
%doc %{_texmfdistdir}/source/latex/textpos

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
