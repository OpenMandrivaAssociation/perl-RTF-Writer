%define upstream_name    RTF-Writer
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    for generating documents in Rich Text Format
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/RTF/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Path)
BuildRequires: perl(Image::Size)
BuildRequires: perl(UNIVERSAL)
BuildRequires: perl(strict)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
