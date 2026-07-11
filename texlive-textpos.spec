%global tl_name textpos
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10.1
Release:	%{tl_revision}.1
Summary:	Place boxes at arbitrary positions on the LaTeX page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textpos
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textpos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textpos.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textpos.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to facilitate the placement of boxes at absolute positions on
the LaTeX page. There are several reasons why this might be useful, one
important example being to help the creation of large-format conference
posters.

