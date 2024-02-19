# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate msru

Name:           rust-msru
Version:        0.2.0
Release:        %autorelease
Summary:        Rust-safe library for interacting with Model Specific Registers in user-space

License:        Apache-2.0
URL:            https://crates.io/crates/msru
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * fix typo in crate description
Patch:          msru-fix-metadata.diff

ExclusiveArch:  x86_64 riscv64
BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A Rust-safe library for interacting with Model Specific Registers in
user-space.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
