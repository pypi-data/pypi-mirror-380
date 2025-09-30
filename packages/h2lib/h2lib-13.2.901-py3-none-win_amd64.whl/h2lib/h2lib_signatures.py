# noqa

from h2lib.dll_wrapper import DLLWrapper


class H2LibSignatures():
    def _add_distributed_sections(self, mainbody_nr, nsec, sec_rel_pos, link_id, check_stop=True):
        '''subroutine add_distributed_sections(mainbody_nr, nsec, sec_rel_pos, link_id) bind(C, name="add_distributed_sections")
      integer*8, intent(in) :: mainbody_nr, nsec
      integer*8, intent(out) :: link_id
      real(c_double), intent(in) :: sec_rel_pos(nsec)
    end subroutine'''
        return self.get_lib_function('add_distributed_sections')(mainbody_nr, nsec, sec_rel_pos, link_id, check_stop=check_stop)

    def _add_sensor(self, sensor_line, index_start, index_stop, check_stop=True):
        '''subroutine add_sensor(sensor_line, index_start, index_stop) bind(C, name="add_sensor")
      integer*8 :: index_start, index_stop
      character(kind=c_char, len=1), intent(in)       :: sensor_line(1024)
    end subroutine'''
        return self.get_lib_function('add_sensor')(sensor_line, index_start, index_stop, check_stop=check_stop)

    def _body_output_element(self, ibdy, ielem, mass, stiffness, damping, error_code, check_stop=True):
        '''subroutine body_output_element(ibdy, ielem, mass, stiffness, damping, error_code) &
    integer(kind=4), intent(in) :: ibdy
    integer(kind=4), intent(in) :: ielem
    real(kind=c_double), dimension(12, 12), intent(out) :: mass
    real(kind=c_double), dimension(12, 12), intent(out) :: stiffness
    real(kind=c_double), dimension(12, 12), intent(out) :: damping
    integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('body_output_element')(ibdy, ielem, mass, stiffness, damping, error_code, check_stop=check_stop)

    def _body_output_mass(self, ibdy, body_mass, body_inertia, cog_global_frame, cog_body_frame, error_code, check_stop=True):
        '''subroutine body_output_mass(ibdy, body_mass, body_inertia, cog_global_frame, cog_body_frame, error_code) &
    integer(kind=4), intent(in) :: ibdy
    real(kind=c_double), intent(out) :: body_mass
    real(kind=c_double), intent(out) :: body_inertia(6)
    real(kind=c_double), intent(out) :: cog_global_frame(3)
    real(kind=c_double), intent(out) :: cog_body_frame(3)
    integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('body_output_mass')(ibdy, body_mass, body_inertia, cog_global_frame, cog_body_frame, error_code, check_stop=check_stop)

    def _check_convergence(self, bconv, resq, resg, resd, check_stop=True):
        '''subroutine check_convergence(bconv, resq, resg, resd) bind(C, name='check_convergence')
      logical(kind=c_bool), intent(out) :: bconv
      real(c_double), intent(out) :: resq
      real(c_double), intent(out) :: resg
      real(c_double), intent(out) :: resd
    end subroutine'''
        return self.get_lib_function('check_convergence')(bconv, resq, resg, resd, check_stop=check_stop)

    def _do_system_eigenanalysis(self, include_damping, n_modes, natural_frequencies, damping_ratios, error_code, check_stop=True):
        '''subroutine do_system_eigenanalysis(include_damping, n_modes, natural_frequencies, damping_ratios, error_code) &
logical(kind=c_bool), intent(in) :: include_damping
integer(kind=4), intent(in) :: n_modes
real(kind=c_double), dimension(n_modes), intent(out) :: natural_frequencies
real(kind=c_double), dimension(n_modes), intent(out) :: damping_ratios
integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('do_system_eigenanalysis')(include_damping, n_modes, natural_frequencies, damping_ratios, error_code, check_stop=check_stop)

    def _finalize(self, check_stop=True):
        '''SUBROUTINE finalize() bind(C, name="finalize")
!DEC$ ATTRIBUTES DLLEXPORT :: finalize
  integer:: i
  real*4:: T2
END SUBROUTINE'''
        return self.get_lib_function('finalize')(check_stop=check_stop)

    def _getState(self, restype, check_stop=True):
        '''function getState() result(val) BIND(C, NAME='getState')
  !DEC$ ATTRIBUTES DLLEXPORT :: getState
        integer             :: val
    end function'''
        return self.get_lib_function('getState')(restype=restype, check_stop=check_stop)

    def _get_aerosections_forces(self, rotor, Fxyz, check_stop=True):
        '''subroutine get_aerosections_forces(rotor, Fxyz) bind(C, name='get_aerosections_forces')
    integer*8, intent(in) :: rotor
    real(c_double),intent(out)::Fxyz(rotors_gl%rotor(rotor)%nbld, rotors_gl%rotor(rotor)%blade(1)%nsec, 3)
  end subroutine'''
        return self.get_lib_function('get_aerosections_forces')(rotor, Fxyz, check_stop=check_stop)

    def _get_aerosections_moments(self, rotor, Mxyz, check_stop=True):
        '''subroutine get_aerosections_moments(rotor, Mxyz) bind(C, name='get_aerosections_moments')
    integer*8, intent(in) :: rotor
    real(c_double),intent(out):: Mxyz(rotors_gl%rotor(rotor)%nbld, rotors_gl%rotor(rotor)%blade(1)%nsec, 3)
  end subroutine'''
        return self.get_lib_function('get_aerosections_moments')(rotor, Mxyz, check_stop=check_stop)

    def _get_aerosections_position(self, rotor, position, check_stop=True):
        '''subroutine get_aerosections_position(rotor, position) bind(C, name="get_aerosections_position")
    integer*8, intent(in) :: rotor
    real(c_double),intent(out)   :: position(rotors_gl%rotor(rotor)%nbld, rotors_gl%rotor(rotor)%blade(1)%nsec, 3)
  end subroutine'''
        return self.get_lib_function('get_aerosections_position')(rotor, position, check_stop=check_stop)

    def _get_bem_grid(self, rotor, azi, rad, check_stop=True):
        '''subroutine get_bem_grid(rotor, azi, rad) bind(C, name="get_bem_grid")
    integer*8, intent(in)               :: rotor
    real(c_double), intent(out)       :: azi(rotors_gl%rotor(rotor)%dyn_induc%bem%nazi)
    real(c_double), intent(out)       :: rad(rotors_gl%rotor(rotor)%dyn_induc%bem%nrad)
  end subroutine'''
        return self.get_lib_function('get_bem_grid')(rotor, azi, rad, check_stop=check_stop)

    def _get_bem_grid_dim(self, rotor, nazi, nrad, check_stop=True):
        '''subroutine get_bem_grid_dim(rotor, nazi, nrad) bind(C, name="get_bem_grid_dim")
    integer*8, intent(in)               :: rotor
    integer*8, intent(out)              :: nazi, nrad
  end subroutine'''
        return self.get_lib_function('get_bem_grid_dim')(rotor, nazi, nrad, check_stop=check_stop)

    def _get_body_rotation_tensor(self, ibdy, amat, error_code, check_stop=True):
        '''subroutine get_body_rotation_tensor(ibdy, amat, error_code) &
    integer(kind=8), intent(in) :: ibdy
    real(kind=c_double), dimension(3, 3), intent(out) :: amat
    integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_body_rotation_tensor')(ibdy, amat, error_code, check_stop=check_stop)

    def _get_diameter(self, rotor, restype, check_stop=True):
        '''function get_diameter(rotor) bind(C, name="get_diameter")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_diameter
    integer*8, intent(in) :: rotor
    Type (Taerorotor),pointer :: rotor_p
    real(c_double)  :: get_diameter
 end function'''
        return self.get_lib_function('get_diameter')(rotor, restype=restype, check_stop=check_stop)

    def _get_distributed_section_force_and_moment(self, link_type, link_id, nsec, frc, mom, mainbody_coo_nr, check_stop=True):
        '''subroutine get_distributed_section_force_and_moment(link_type, link_id, nsec, frc, mom, mainbody_coo_nr) bind(C, name="get_distributed_section_force_and_moment")
      integer*8, intent(in) ::  link_type, link_id, nsec, mainbody_coo_nr
      real(c_double), intent(out) :: frc(nsec,3), mom(nsec,3)
    end subroutine'''
        return self.get_lib_function('get_distributed_section_force_and_moment')(link_type, link_id, nsec, frc, mom, mainbody_coo_nr, check_stop=check_stop)

    def _get_distributed_section_position_orientation(self, link_type, link_id, nsec, sec_pos, sec_ori, mainbody_coo_nr, check_stop=True):
        '''subroutine get_distributed_section_position_orientation(link_type, link_id, nsec, sec_pos, sec_ori, mainbody_coo_nr) bind(C, name="get_distributed_section_position_orientation")
      integer*8, intent(in) ::  link_type, link_id, nsec, mainbody_coo_nr
      real(c_double), intent(out) :: sec_pos(nsec,3)
      real(c_double), intent(out) :: sec_ori(nsec,3,3)
    end subroutine'''
        return self.get_lib_function('get_distributed_section_position_orientation')(link_type, link_id, nsec, sec_pos, sec_ori, mainbody_coo_nr, check_stop=check_stop)

    def _get_distributed_sections(self, link_type, link_id, mainbody_nr, nsec, check_stop=True):
        '''subroutine get_distributed_sections(link_type, link_id, mainbody_nr, nsec) bind(C, name="get_distributed_sections")
      integer*8, intent(in) :: link_type, link_id
      integer*8, intent(out) :: nsec, mainbody_nr
    end subroutine'''
        return self.get_lib_function('get_distributed_sections')(link_type, link_id, mainbody_nr, nsec, check_stop=check_stop)

    def _get_induction_axisymmetric(self, rotor, induction, check_stop=True):
        '''subroutine get_induction_axisymmetric(rotor, induction) bind(C, name="get_induction_axisymmetric")
    integer*8, intent(in)        :: rotor
    real(c_double),intent(out)   :: induction(rotors_gl%rotor(rotor)%dyn_induc%bem%nrad)
  end subroutine'''
        return self.get_lib_function('get_induction_axisymmetric')(rotor, induction, check_stop=check_stop)

    def _get_induction_polargrid(self, rotor, induction, check_stop=True):
        '''subroutine get_induction_polargrid(rotor, induction) bind(C, name="get_induction_polargrid")
      integer*8, intent(in)        :: rotor
      real(c_double),intent(out)   :: induction(rotors_gl%rotor(rotor)%dyn_induc%bem%nazi, rotors_gl%rotor(rotor)%dyn_induc%bem%nrad)
  end subroutine'''
        return self.get_lib_function('get_induction_polargrid')(rotor, induction, check_stop=check_stop)

    def _get_induction_rotoravg(self, rotor, induction, check_stop=True):
        '''subroutine get_induction_rotoravg(rotor, induction) bind(C, name="get_induction_rotoravg")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_induction_rotoravg
    integer*8, intent(in)        :: rotor
    real(c_double), intent(out) :: induction
  end subroutine'''
        return self.get_lib_function('get_induction_rotoravg')(rotor, induction, check_stop=check_stop)

    def _get_mainbody_name(self, mainbody_nr, mainbody_name, check_stop=True):
        '''subroutine get_mainbody_name(mainbody_nr, mainbody_name) bind(C, name="get_mainbody_name")
      integer*8 :: mainbody_nr
      character(kind=c_char, len=1), intent(out) :: mainbody_name(256)
    end subroutine'''
        return self.get_lib_function('get_mainbody_name')(mainbody_nr, mainbody_name, check_stop=check_stop)

    def _get_mainbody_nnodes(self, mainbody_nr, restype, check_stop=True):
        '''function get_mainbody_nnodes(mainbody_nr) bind(C, name="get_mainbody_nnodes")
      !dec$ attributes dllexport :: get_mainbody_nnodes
      integer*8, intent(in) :: mainbody_nr
      integer*8 :: get_mainbody_nnodes
    end function'''
        return self.get_lib_function('get_mainbody_nnodes')(mainbody_nr, restype=restype, check_stop=check_stop)

    def _get_mainbody_nodes_state(self, mainbody_nr, state, nnodes, mainbody_coo_nr, nodes_state, check_stop=True):
        '''subroutine get_mainbody_nodes_state(mainbody_nr, state, nnodes, mainbody_coo_nr, nodes_state) bind(C, name="get_mainbody_nodes_state")
      integer*8, intent(in) :: mainbody_nr, state, nnodes, mainbody_coo_nr
      real(c_double), intent(out) :: nodes_state(nnodes,3)
    end subroutine'''
        return self.get_lib_function('get_mainbody_nodes_state')(mainbody_nr, state, nnodes, mainbody_coo_nr, nodes_state, check_stop=check_stop)

    def _get_mainbody_position_orientation(self, mainbody_nr, mbdy_pos, mbdy_ori, mainbody_coo_nr, check_stop=True):
        '''subroutine get_mainbody_position_orientation(mainbody_nr, mbdy_pos, mbdy_ori, mainbody_coo_nr) bind(C, name="get_mainbody_position_orientation")
      integer*8, intent(in) :: mainbody_nr, mainbody_coo_nr
      real(c_double), intent(out) :: mbdy_pos(3)
      real(c_double), intent(out) :: mbdy_ori(3,3)
    end subroutine'''
        return self.get_lib_function('get_mainbody_position_orientation')(mainbody_nr, mbdy_pos, mbdy_ori, mainbody_coo_nr, check_stop=check_stop)

    def _get_nSections(self, rotor, blade, restype, check_stop=True):
        '''function get_nSections(rotor, blade) bind(C, name="get_nSections")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_nSections
    integer*8, intent(in) :: rotor, blade
    integer*8             :: get_nSections
  end function'''
        return self.get_lib_function('get_nSections')(rotor, blade, restype=restype, check_stop=check_stop)

    def _get_nblades(self, rotor, restype, check_stop=True):
        '''function get_nblades(rotor) bind(C, name="get_nblades")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_nblades
    integer*8, intent(in) ::  rotor
    integer*8             :: get_nblades
  end function'''
        return self.get_lib_function('get_nblades')(rotor, restype=restype, check_stop=check_stop)

    def _get_nrotors(self, restype, check_stop=True):
        '''function get_nrotors() bind(C, name="get_nrotors")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_nrotors
    integer*8 :: get_nrotors
  end function'''
        return self.get_lib_function('get_nrotors')(restype=restype, check_stop=check_stop)

    def _get_number_of_bodies_and_constraints(self, nbdy, ncst, error_code, check_stop=True):
        '''subroutine get_number_of_bodies_and_constraints(nbdy, ncst, error_code) &
    integer(kind=8), intent(out) :: nbdy
    integer(kind=8), intent(out) :: ncst
    integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_number_of_bodies_and_constraints')(nbdy, ncst, error_code, check_stop=check_stop)

    def _get_number_of_elements(self, nbdy, nelem, error_code, check_stop=True):
        '''subroutine get_number_of_elements(nbdy, nelem, error_code) &
    integer(kind=8), intent(in) :: nbdy
    integer(kind=8), dimension(nbdy), intent(out) :: nelem
    integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_number_of_elements')(nbdy, nelem, error_code, check_stop=check_stop)

    def _get_number_of_mainbodies(self, restype, check_stop=True):
        '''function get_number_of_mainbodies() bind(C, name="get_number_of_mainbodies")
      !DEC$ ATTRIBUTES DLLEXPORT :: get_number_of_mainbodies
      integer*8 :: get_number_of_mainbodies
    end function'''
        return self.get_lib_function('get_number_of_mainbodies')(restype=restype, check_stop=check_stop)

    def _get_rotor_avg_wsp(self, coo, rotor, wsp, check_stop=True):
        '''subroutine get_rotor_avg_wsp(coo, rotor, wsp) bind(C, name="get_rotor_avg_wsp")
    integer*8, intent(in) :: rotor
    integer*8, intent(in) :: coo ! 1: global, 2: rotor
    real(c_double), dimension(3):: wsp
  end subroutine'''
        return self.get_lib_function('get_rotor_avg_wsp')(coo, rotor, wsp, check_stop=check_stop)

    def _get_rotor_orientation(self, rotor, yaw, tilt, azi, check_stop=True):
        '''subroutine get_rotor_orientation(rotor, yaw, tilt, azi) bind(C, name="get_rotor_orientation")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_rotor_orientation
    integer*8, intent(in) :: rotor
    real(c_double), intent(out) :: yaw, tilt, azi
  end subroutine'''
        return self.get_lib_function('get_rotor_orientation')(rotor, yaw, tilt, azi, check_stop=check_stop)

    def _get_rotor_position(self, rotor, position, check_stop=True):
        '''subroutine get_rotor_position(rotor, position) bind(C, name="get_rotor_position")
    !DEC$ ATTRIBUTES DLLEXPORT :: get_rotor_position
    integer*8, intent(in) :: rotor
    real(c_double), dimension(3), intent(out) ::  position
  !DEC$ ATTRIBUTES DLLEXPORT :: get_rotor_avg_wsp
    integer*8, intent(in) :: rotor
    integer*8, intent(in) :: coo ! 1: global, 2: rotor
  end subroutine'''
        return self.get_lib_function('get_rotor_position')(rotor, position, check_stop=check_stop)

    def _get_sensor_info(self, id, name, unit, desc, check_stop=True):
        '''subroutine get_sensor_info(id, name, unit, desc) bind(C, name="get_sensor_info")
      integer*8, intent(in) :: id
      character(kind=c_char, len=1), intent(out)       :: name(30), unit(10), desc(512)
    end subroutine'''
        return self.get_lib_function('get_sensor_info')(id, name, unit, desc, check_stop=check_stop)

    def _get_sensor_values(self, ids, values, n, check_stop=True):
        '''subroutine get_sensor_values(ids, values, n) bind(C, name="get_sensor_values")
      integer*8, intent(in) :: n
      integer*8, intent(in) :: ids(n)
      real(c_double), intent(out)        :: values(n)
    end subroutine'''
        return self.get_lib_function('get_sensor_values')(ids, values, n, check_stop=check_stop)

    def _get_system_eigval_eigvec_with_damping(self, n_modes, ny, eigenvalues, eigenvectors, error_code, check_stop=True):
        '''subroutine get_system_eigval_eigvec_with_damping(n_modes, ny, eigenvalues, eigenvectors, error_code) &
integer(kind=4), intent(in) :: n_modes
integer(kind=4), intent(in) :: ny
complex(kind=c_double_complex), dimension(n_modes), intent(out) :: eigenvalues
complex(kind=c_double_complex), dimension(ny, n_modes), intent(out) :: eigenvectors
integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_system_eigval_eigvec_with_damping')(n_modes, ny, eigenvalues, eigenvectors, error_code, check_stop=check_stop)

    def _get_system_eigval_eigvec_without_damping(self, n_modes, ny, eigenvalues, eigenvectors, error_code, check_stop=True):
        '''subroutine get_system_eigval_eigvec_without_damping(n_modes, ny, eigenvalues, eigenvectors, error_code) &
integer(kind=4), intent(in) :: n_modes
integer(kind=4), intent(in) :: ny
real(kind=c_double), dimension(n_modes), intent(out) :: eigenvalues
real(kind=c_double), dimension(ny, n_modes), intent(out) :: eigenvectors
integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_system_eigval_eigvec_without_damping')(n_modes, ny, eigenvalues, eigenvectors, error_code, check_stop=check_stop)

    def _get_system_matrices(self, n_tdofs, n_rdofs, M, C, K, R, error_code, check_stop=True):
        '''subroutine get_system_matrices(n_tdofs, n_rdofs, M, C, K, R, error_code) &
integer(kind=4), intent(in) :: n_tdofs
integer(kind=4), intent(in) :: n_rdofs
real(kind=c_double), dimension(n_rdofs, n_rdofs), intent(out) :: M
real(kind=c_double), dimension(n_rdofs, n_rdofs), intent(out) :: C
real(kind=c_double), dimension(n_rdofs, n_rdofs), intent(out) :: K
real(kind=c_double), dimension(n_tdofs, n_rdofs), intent(out) :: R
integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_system_matrices')(n_tdofs, n_rdofs, M, C, K, R, error_code, check_stop=check_stop)

    def _get_time(self, time, check_stop=True):
        '''subroutine
subroutine'''
        return self.get_lib_function('get_time')(time, check_stop=check_stop)

    def _get_timoshenko_location(self, ibdy, ielem, l, r1, r12, tes, error_code, check_stop=True):
        '''subroutine get_timoshenko_location(ibdy, ielem, l, r1, r12, tes, error_code) &
    integer(kind=8), intent(in) :: ibdy
    integer(kind=8), intent(in) :: ielem
    real(kind=c_double), intent(out) :: l
    real(kind=c_double), dimension(3), intent(out) :: r1
    real(kind=c_double), dimension(3), intent(out) :: r12
    real(kind=c_double), dimension(3,3), intent(out) :: tes
    integer(kind=8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('get_timoshenko_location')(ibdy, ielem, l, r1, r12, tes, error_code, check_stop=check_stop)

    def _get_version(self, s, check_stop=True):
        '''subroutine get_version(s) BIND(C, NAME='get_version')
                character(kind=c_char, len=1), intent(inout)  :: s(255)
            end subroutine'''
        return self.get_lib_function('get_version')(s, check_stop=check_stop)

    def _init(self, check_stop=True):
        '''subroutine init() bind(C, name="init")
     !DEC$ ATTRIBUTES DLLEXPORT :: init
    end subroutine'''
        return self.get_lib_function('init')(check_stop=check_stop)

    def _init_AD(self, rotor, tiploss_method, tiploss2_shen_c2, tiploss2_shen_h, check_stop=True):
        '''subroutine init_AD(rotor, tiploss_method, tiploss2_shen_c2, tiploss2_shen_h) bind(C, name="init_AD")
    integer*8, intent(in) :: rotor
    integer*8, intent(in) :: tiploss_method
    REAL(c_double), intent(in) :: tiploss2_shen_c2, tiploss2_shen_h
  end subroutine'''
        return self.get_lib_function('init_AD')(rotor, tiploss_method, tiploss2_shen_c2, tiploss2_shen_h, check_stop=check_stop)

    def _init_AL(self, rotor, epsilon_smearing, check_stop=True):
        '''subroutine init_AL(rotor, epsilon_smearing) bind(C, name="init_AL")
    real(c_double), intent(in) :: epsilon_smearing
    integer*8, intent(in) :: rotor
  end subroutine'''
        return self.get_lib_function('init_AL')(rotor, epsilon_smearing, check_stop=check_stop)

    def _init_windfield(self, Nxyz, dxyz, box_offset_yz, transport_speed, check_stop=True):
        '''subroutine init_windfield(Nxyz, dxyz, box_offset_yz, transport_speed) bind(C, name="init_windfield")
      integer*8, dimension(3), intent(in) :: Nxyz
      real*8              :: transport_speed
    end subroutine'''
        return self.get_lib_function('init_windfield')(Nxyz, dxyz, box_offset_yz, transport_speed, check_stop=check_stop)

    def _initialize_distributed_sections(self, check_stop=True):
        '''subroutine initialize_distributed_sections() bind(C, name="initialize_distributed_sections")
      !DEC$ ATTRIBUTES DLLEXPORT :: initialize_distributed_sections
      type (Tseclink), dimension(:), pointer :: seclinks
      type (Tbaselink) :: baselink
      type (body_type), dimension(:), pointer :: b_vec
      integer :: i
    end subroutine'''
        return self.get_lib_function('initialize_distributed_sections')(check_stop=check_stop)

    def _linearize(self, n_tdofs, n_rdofs, check_stop=True):
        '''subroutine linearize(n_tdofs, n_rdofs) bind(C, name="linearize")
integer(kind=8), intent(out) :: n_tdofs
integer(kind=8), intent(out) :: n_rdofs
end subroutine'''
        return self.get_lib_function('linearize')(n_tdofs, n_rdofs, check_stop=check_stop)

    def _loop(self, N, restype, check_stop=True):
        '''function loop(N) bind(C, Name='loop')
    !DEC$ ATTRIBUTES DLLEXPORT :: loop
    integer*8, intent(in) :: N
    real(c_double) :: loop,a
    integer*8 :: i, j
  end function'''
        return self.get_lib_function('loop')(N, restype=restype, check_stop=check_stop)

    def _read_input(self, htc_path, check_stop=True):
        '''subroutine read_input(htc_path) bind(C, name="read_input")
      character(kind=c_char, len=1), intent(in)       :: htc_path(1024)
    end subroutine'''
        return self.get_lib_function('read_input')(htc_path, check_stop=check_stop)

    def _run(self, time, restype, check_stop=True):
        '''function run(time) bind(C, name='run')
      !DEC$ ATTRIBUTES DLLEXPORT :: run
      real(c_double), intent(in) :: time
      real(c_double) :: run, eps
    end function'''
        return self.get_lib_function('run')(time, restype=restype, check_stop=check_stop)

    def _set_aerosections_windspeed(self, rotor, uvw, check_stop=True):
        '''subroutine set_aerosections_windspeed(rotor, uvw) bind(C, name="set_aerosections_windspeed")
    integer*8, intent(in) :: rotor
    real(c_double),intent(in)   :: uvw(rotors_gl%rotor(rotor)%nbld, rotors_gl%rotor(rotor)%blade(1)%nsec, 3)
  end subroutine'''
        return self.get_lib_function('set_aerosections_windspeed')(rotor, uvw, check_stop=check_stop)

    def _set_cx_def(self, mainbody_nr, nsec, n_cols, cx_def, twist_in_deg, check_length, update_structure, error_code, check_stop=True):
        '''subroutine set_cx_def(mainbody_nr, nsec, n_cols, cx_def, twist_in_deg, check_length, update_structure, error_code) bind(C, name="set_cx_def")
integer(kind=8),                                        intent(in   ) :: mainbody_nr
integer(kind=4),                                        intent(in   ) :: nsec, n_cols
real(kind=c_double),           dimension(nsec, n_cols), intent(in   ) :: cx_def
logical(kind=c_bool),                                   intent(in   ) :: twist_in_deg
logical(kind=c_bool),                                   intent(in   ) :: check_length
logical,                                                intent(in   ) :: update_structure
integer(kind=8),                                        intent(  out) :: error_code
end subroutine'''
        return self.get_lib_function('set_cx_def')(mainbody_nr, nsec, n_cols, cx_def, twist_in_deg, check_length, update_structure, error_code, check_stop=check_stop)

    def _set_distributed_section_force_and_moment(self, link_type, link_id, nsec, frc, mom, mainbody_coo_nr, check_stop=True):
        '''subroutine set_distributed_section_force_and_moment(link_type, link_id, nsec, frc, mom, mainbody_coo_nr) bind(C, name="set_distributed_section_force_and_moment")
      integer*8, intent(in) ::  link_type, link_id, nsec
      integer*8, intent(in) ::  mainbody_coo_nr ! -1: section, 0: global, >0: mainbody nr
      real(c_double), intent(inout) :: frc(nsec,3), mom(nsec,3)
    end subroutine'''
        return self.get_lib_function('set_distributed_section_force_and_moment')(link_type, link_id, nsec, frc, mom, mainbody_coo_nr, check_stop=check_stop)

    def _set_orientation_base(self, main_body_name, n_rows, mbdy_eulerang_table, angles_in_deg, reset_orientation, mbdy_ini_rotvec_d1, error_code, check_stop=True):
        '''subroutine set_orientation_base(main_body_name, n_rows, mbdy_eulerang_table, angles_in_deg, reset_orientation, mbdy_ini_rotvec_d1, error_code) &
character(kind=c_char, len=1), dimension(256), intent(in) :: main_body_name
integer(kind=4), intent(in) :: n_rows
real(kind=c_double), dimension(n_rows, 3),   intent(in) :: mbdy_eulerang_table
logical(c_bool), intent(in) :: angles_in_deg
logical(c_bool), intent(in) :: reset_orientation
real(kind=c_double), dimension(4),   intent(in) :: mbdy_ini_rotvec_d1
integer(kind=8), intent(out) :: error_code  ! Error code.
end subroutine'''
        return self.get_lib_function('set_orientation_base')(main_body_name, n_rows, mbdy_eulerang_table, angles_in_deg, reset_orientation, mbdy_ini_rotvec_d1, error_code, check_stop=check_stop)

    def _set_orientation_relative(self, main_body_1_name, node_1, main_body_2_name, node_2, n_rows, mbdy2_eulerang_table, angles_in_deg, reset_orientation, mbdy2_ini_rotvec_d1, error_code, check_stop=True):
        '''subroutine set_orientation_relative(main_body_1_name, node_1, main_body_2_name, node_2, n_rows, mbdy2_eulerang_table, angles_in_deg, reset_orientation, mbdy2_ini_rotvec_d1, error_code) &
character(kind=c_char, len=1),   dimension(256),       intent(in   ) :: main_body_1_name  ! Defined as an array of length 1 characters because of bind.
character(kind=c_char, len=1),   dimension(256),       intent(in   ) :: main_body_2_name  ! Defined as an array of length 1 characters because of bind.
integer(kind=8),                                       intent(in   ) :: node_1
integer(kind=8),                                       intent(in   ) :: node_2
integer(kind=4),                                       intent(in   ) :: n_rows
real(kind=c_double),             dimension(n_rows, 3), intent(in   ) :: mbdy2_eulerang_table
logical(c_bool),                                       intent(in   ) :: angles_in_deg
logical(c_bool),                                       intent(in   ) :: reset_orientation
real(kind=c_double),             dimension(4),         intent(in   ) :: mbdy2_ini_rotvec_d1  ! Initial angular velocity direction and magnitude.
integer(kind=8),                                       intent(  out) :: error_code
character(kind=c_char, len=256) :: mbdy_1_name  ! Same as main_body_1_name, but as string instead of an array of characters.
character(kind=c_char, len=256) :: mbdy_2_name  ! Same as main_body_2_name, but as string instead of an array of characters.
type(Tmain_body_input), pointer :: main_body_1  ! The main body pointer associated to main_body_1_name.
type(Tmain_body_input), pointer :: main_body_2  ! The main body pointer associated to main_body_1_name.
integer(kind=4) :: node_1_local, node_2_local     ! Internal copy of node_1 and node_2.
real*8, dimension(3) :: eulerang                ! Euler angles associated to 1 row of mbdy2_eulerang_table.
end subroutine'''
        return self.get_lib_function('set_orientation_relative')(main_body_1_name, node_1, main_body_2_name, node_2, n_rows, mbdy2_eulerang_table, angles_in_deg, reset_orientation, mbdy2_ini_rotvec_d1, error_code, check_stop=check_stop)

    def _set_st(self, mainbody_nr, n_rows, n_cols, st, update_structure, error_code, check_stop=True):
        '''subroutine set_st(mainbody_nr, n_rows, n_cols, st, update_structure, error_code) bind(C, name="set_st")
integer(kind=8),                                 intent(in   ) :: mainbody_nr
integer(kind=4),                                 intent(in   ) :: n_rows
integer(kind=4),                                 intent(in   ) :: n_cols
real(kind=c_double),  dimension(n_rows, n_cols), intent(in   ) :: st
logical,                                         intent(in   ) :: update_structure
integer(kind=8),                                 intent(  out) :: error_code
type(Tmain_body_input), pointer :: main_body  ! The main body whose st we want to update.
end subroutine'''
        return self.get_lib_function('set_st')(mainbody_nr, n_rows, n_cols, st, update_structure, error_code, check_stop=check_stop)

    def _set_variable_sensor_value(self, id, value, check_stop=True):
        '''subroutine set_variable_sensor_value(id, value) bind(C, name="set_variable_sensor_value")
      integer*8, intent(in) :: id
      real(c_double)        :: value
    end subroutine'''
        return self.get_lib_function('set_variable_sensor_value')(id, value, check_stop=check_stop)

    def _set_windfield(self, uvw, box_offset_x, time, check_stop=True):
        '''subroutine set_windfield(uvw, box_offset_x, time) bind(C, name="set_windfield")
      real*4, intent(in) :: uvw(3, gwsd%TMOD%buffer_points_x,gwsd%TMOD%buffer_points_y,gwsd%TMOD%buffer_points_z)
      real*8, intent(in):: box_offset_x, time
    end subroutine'''
        return self.get_lib_function('set_windfield')(uvw, box_offset_x, time, check_stop=check_stop)

    def _solver_static_delete(self, check_stop=True):
        '''subroutine solver_static_delete() &
    !DEC$ ATTRIBUTES DLLEXPORT :: solver_static_delete
end subroutine'''
        return self.get_lib_function('solver_static_delete')(check_stop=check_stop)

    def _solver_static_init(self, check_stop=True):
        '''subroutine solver_static_init() &
    !DEC$ ATTRIBUTES DLLEXPORT :: solver_static_init
end subroutine'''
        return self.get_lib_function('solver_static_init')(check_stop=check_stop)

    def _solver_static_run(self, reset_structure, error_code, check_stop=True):
        '''subroutine solver_static_run(reset_structure, error_code) bind(C, name="solver_static_run")
    logical(c_bool), intent(in) :: reset_structure
    integer(8), intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('solver_static_run')(reset_structure, error_code, check_stop=check_stop)

    def _solver_static_solve(self, error_code, check_stop=True):
        '''subroutine solver_static_solve(error_code) &
    integer*8, intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('solver_static_solve')(error_code, check_stop=check_stop)

    def _solver_static_update(self, error_code, check_stop=True):
        '''subroutine solver_static_update(error_code) &
    integer*8, intent(out) :: error_code
end subroutine'''
        return self.get_lib_function('solver_static_update')(error_code, check_stop=check_stop)

    def _step(self, restype, check_stop=True):
        '''function step() bind(C, name='step')
      !DEC$ ATTRIBUTES DLLEXPORT :: step
      real(c_double) :: step
    end function'''
        return self.get_lib_function('step')(restype=restype, check_stop=check_stop)

    def _stop_on_error(self, flag, check_stop=True):
        '''subroutine stop_on_error(flag) bind(C, name="stop_on_error")
  logical(c_bool), intent(in) :: flag
end subroutine'''
        return self.get_lib_function('stop_on_error')(flag, check_stop=check_stop)

    def _structure_reset(self, check_stop=True):
        '''subroutine structure_reset() bind(C, name="structure_reset")
    !DEC$ ATTRIBUTES DLLEXPORT :: structure_reset
    integer*4 :: i, j
end subroutine'''
        return self.get_lib_function('structure_reset')(check_stop=check_stop)

    def _work(self, time, restype, check_stop=True):
        '''function work(time) bind(C, Name='work')
    !DEC$ ATTRIBUTES DLLEXPORT :: work
    real(c_double), intent(in) :: time
    real*4 :: start_time, t
    integer*8 :: N, work
  end function'''
        return self.get_lib_function('work')(time, restype=restype, check_stop=check_stop)

    def _write_output(self, check_stop=True):
        '''subroutine write_output() bind(C, name="write_output")
      !DEC$ ATTRIBUTES DLLEXPORT :: write_output
      integer        :: nr, dummy=1
      character*10 :: status = 'close'
      Type (Toutvar) :: ov_dummy
    end subroutine'''
        return self.get_lib_function('write_output')(check_stop=check_stop)
