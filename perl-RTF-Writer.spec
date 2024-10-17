%define upstream_name    RTF-Writer
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    for generating documents in Rich Text Format
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/RTF/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Path)
BuildRequires: perl(Image::Size)
BuildRequires: perl(UNIVERSAL)
BuildRequires: perl(strict)
BuildRequires: perl-devel
BuildArch: noarch

%description
This module is for generating documents in Rich Text Format. 

This module is a class; an object belonging to this class acts like an
output filehandle, and calling methods on it causes RTF text to be written.

Incidentally, this module also exports a few useful functions, upon
request.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.110.0-2mdv2011.0
+ Revision: 658877
- rebuild for updated spec-helper

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 404359
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.11-4mdv2009.0
+ Revision: 258331
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.11-3mdv2009.0
+ Revision: 246409
- rebuild

* Mon Mar 03 2008 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2008.1
+ Revision: 178007
- import perl-RTF-Writer


