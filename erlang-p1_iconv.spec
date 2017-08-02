%global srcname p1_iconv
# Erlang packages don't seem to ship debug files, as the build process does not generate them
%global debug_package %{nil}
%define _disable_ld_no_undefined 1

Name:       erlang-%{srcname}
Version:    0.9.0
Release:    %mkrel 2
Group:      Development/Erlang

Summary:    Fast encoding conversion library for Erlang / Elixir
License:    GPLv2
URL:        https://github.com/processone/iconv/
Source0:    https://github.com/processone/iconv/archive/%{version}.tar.gz

BuildRequires: erlang-rebar


%description
Erlang bindings for iconv. This is used by ejabberd.


%prep
%autosetup -n iconv-%{version}


%build
%configure --enable-nif
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm644 ebin/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -pm755 priv/lib/iconv.so $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/


%files
%license COPYING
%doc README.md
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Sat May 07 2016 neoclust <neoclust> 0.9.0-2.mga6
+ Revision: 1010437
- imported package erlang-p1_iconv

