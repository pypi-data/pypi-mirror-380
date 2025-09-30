from pathlib import Path

from h2lib_tests import tfp
from numpy import testing as npt
import pytest
from scipy.spatial.transform import Rotation as R
from wetb.hawc2.htc_file import HTCFile
from wetb.hawc2.st_file import StFile

from h2lib import H2Lib
from h2lib.distributed_sections import LinkType
from h2lib_tests.dtu10mw import DTU10MWSimple
import matplotlib.pyplot as plt
import numpy as np


class Plot():
    def __init__(self, h2, ds_lst, ax=None):
        self.h2 = h2
        self.ds_lst = ds_lst
        self.ax = ax or plt.figure().add_subplot(projection='3d')

    def __call__(self, label, coo_index=[], h2=None, ds_lst=None, mainbody_coo=0):
        self.h2 = h2 or self.h2
        self.ds_lst = ds_lst or self.ds_lst
        for ds in self.ds_lst:
            sec_pos, sec_tsg = self.h2.get_distributed_section_position_orientation(ds, mainbody_coo_nr=mainbody_coo)
            x, y, z = sec_pos.T
            self.ax.plot(y, x, z, label=f'{label}, {ds.name}')

            for (x, y, z), tsg in zip(sec_pos[coo_index], sec_tsg[coo_index]):
                for (ex, ey, ez), c in zip(tsg.T * 10, 'rgb'):
                    plt.plot([y, y + ey], [x, x + ex], [z, z + ez], c)

    def show(self, show):
        if show:
            plt.axis('equal')
            self.ax.set_zlim([10, -220])
            plt.legend()
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('y')
            self.ax.set_zlabel('z')
            plt.show()
        else:
            plt.close('all')


def test_distributed_sections():
    # apply force on tower and check deflected tower position
    with H2Lib(suppress_output=0) as h2:
        model_path = f"{tfp}DTU_10_MW/"
        htc_path = f"{tfp}DTU_10_MW/htc/DTU_10MW_RWT.htc"
        h2.init(htc_path=htc_path, model_path=model_path)
        ds_lst = [h2.get_distributed_sections(LinkType.BLADE, link_id=i) for i in [1, 2, 3]]
        plot = Plot(h2, ds_lst)
        plot('', slice(None))
        plot.show(0)

        ds = h2.get_distributed_sections(LinkType.BLADE, link_id=2)
        sec_pos, sec_tsg = h2.get_distributed_section_position_orientation(ds, mainbody_coo_nr=0)
        npt.assert_array_almost_equal(sec_pos[40], [70.58938502, -16.98280589, -77.95555399], 6)
        npt.assert_array_almost_equal(sec_tsg[40], [[0.49371347, 0.09098716, 0.86485163],
                                                    [0.12164175, 0.97750846, -0.17228029],
                                                    [-0.86107508, 0.19025917, 0.47154125]], 6)

        with pytest.raises(AssertionError, match=r"'missing' does not exist. Valid names are \['tower',"):
            h2.add_distributed_sections('missing', [0, .4, .8, 1])
        mbdy_name_dict = h2.get_mainbody_name_dict()
        mbdy_name_lst = list(mbdy_name_dict.keys())
        ds_dict = {mbdy_name: h2.add_distributed_sections(mbdy_name, [0, .4, .8, 1])
                   for mbdy_name in mbdy_name_lst}
        h2.initialize_distributed_sections()
        ds_dict['blade1_aero'] = h2.get_distributed_sections(LinkType.BLADE, 1)
        plot = Plot(h2, ds_dict.values())
        plot('test', slice(None), mainbody_coo=mbdy_name_dict['hub2'])
        plot.show(0)
        # print(ds_lst[6].name, ds_lst[3].name)
        # mb_pos, b1_mb_tbg, b1_sec_pos, sec_tsb = h2.get_distributed_section_position_orientation(ds_lst[6])
        # hub_id = h2.get_mainbody_name_dict()['hub1']
        # print(hub_id)
        # print(h2.get_mainbody_position_orientation(hub_id))
        # print(b1_sec_pos[[0, -1]])

        sec_pos, sec_tsb = h2.get_distributed_section_position_orientation(ds_dict['blade1'])
        # print(np.round(mb_pos + [mb_tbg@sp for sp in sec_pos], 1).tolist())

        print(np.round(sec_pos, 1).tolist())
        npt.assert_array_almost_equal(sec_pos, [[-0.0, -6.9, -121.8],
                                                [0.8, -5.7, -156.4],
                                                [0.4, -5.8, -190.9],
                                                [0.1, -6.5, -208.2]], 1)

        sec_pos, sec_tsb = h2.get_distributed_section_position_orientation(ds_dict['blade1_aero'])

        idx = [0, 10, 20, 30, 40, 49]
        print(np.round(sec_pos[idx], 2).tolist())
        npt.assert_array_almost_equal(sec_pos[idx], [[1.3, -6.61, -121.78],
                                                     [1.37, -6.27, -130.32],
                                                     [2.33, -5.65, -152.69],
                                                     [1.51, -5.61, -179.95],
                                                     [0.86, -6.2, -201.24],
                                                     [0.29, -6.53, -208.25]], 2)

        frc = np.zeros((4, 3))
        frc[:, 1] = 100000
        h2.set_distributed_section_force_and_moment(ds_dict['tower'], sec_frc=frc, sec_mom=np.zeros((4, 3)))

        plot = Plot(h2, ds_dict.values())
        plot('t=0')
        h2.run(2)
        plot('t=2')
        plot.show(0)
        np.set_printoptions(linewidth=200)
        sec_pos, sec_tsb = h2.get_distributed_section_position_orientation(ds_dict['tower'])
        # print(np.round(mb_pos + [mb_tbg@sp for sp in sec_pos], 1).tolist())

        npt.assert_array_almost_equal(sec_pos, [[0.0, 0.0, 0.0],
                                                [-0.0, 0.7, -46.2],
                                                [-0.0, 2.4, -92.5],
                                                [0.0, 3.5, -115.6]], 1)


def test_distributed_section_positions():

    mp = Path(tfp) / 'DTU_10_MW/'
    htc_path = mp / 'htc/DTU_10MW_RWT_only_tower.htc'
    st = StFile(mp / 'data/DTU_10MW_RWT_Tower_st.dat')
    st_new = st.main_data_sets[1][1].copy()
    st_new[:, -2] = .4
    st_new[:, -1] = .3
    st.main_data_sets[1][1] = st_new
    st.save(mp / 'data/DTU_10MW_RWT_Tower_st_tmp.dat')
    htc = HTCFile(htc_path)
    htc.new_htc_structure.main_body.timoschenko_input.filename = str(mp / 'data/DTU_10MW_RWT_Tower_st_tmp.dat')
    htc.set_name('DTU_10MW_RWT_only_tower_tmp.htc')
    htc.save()

    with H2Lib() as h2:
        h2.init(htc_path=htc.filename, model_path=htc.modelpath)
        ds = h2.add_distributed_sections(mainbody_name='tower', section_relative_position=[0, .1, .5, 1])
        h2.initialize_distributed_sections()

        ax = plt.figure().add_subplot(projection='3d')
        pos = h2.get_mainbody_nodes_state(1, 'pos')
        npt.assert_array_equal(pos[:, :2].T, [[-0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4],
                                              [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]])
        ax.plot(*pos.T, '.-', label='initial nodes position')

        sec_pos, sec_tsg = h2.get_distributed_section_position_orientation(ds)
        npt.assert_array_almost_equal(sec_pos[:, :2], 0, 10)
        ax.plot(*sec_pos.T, '.-', label='initial distributed sections, c2def')

        st_new[:, -2] = 0.8
        st_new[:, -1] = 0.9

        h2.set_st(main_body_nr=1, st=st_new)

        pos = h2.get_mainbody_nodes_state(1, 'pos')
        npt.assert_array_equal(pos[:, :2].T, [[-0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8],
                                              [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]])
        ax.plot(*pos.T, '.-', label='exy=1, nodes position')

        sec_pos, sec_tsg = h2.get_distributed_section_position_orientation(ds)
        ax.plot(*sec_pos.T, '.-', label='exy=1 distributed sections, c2def')

        plt.legend()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_zlim([0, -120])
        if 0:
            plt.show()
        plt.close('all')

        npt.assert_array_equal(sec_pos[:, :2], 0, 10)


def test_distributed_sections_static_solver():
    with H2Lib() as h2:
        model_path = f"{tfp}DTU_10_MW/"
        htc_path = f"{tfp}DTU_10_MW/htc/DTU_10MW_RWT_only_tower.htc"
        h2.init(htc_path=htc_path, model_path=model_path)
        ds = h2.add_distributed_sections(mainbody_name='tower', section_relative_position=[0, .5, 1])
        h2.initialize_distributed_sections()

        ax = plt.figure().add_subplot(projection='3d')

        def draw(label, ref):
            pos = h2.get_mainbody_nodes_state(mainbody_nr=1, state='pos')
            # print(label, np.round(pos[-1], 4).tolist())
            npt.assert_array_almost_equal(pos[-1], ref, 4)
            ax.plot(*pos.T, marker='.', label=label)
            ax.set_zlim([0, -120])

        pos = h2.get_mainbody_nodes_state(mainbody_nr=1, state='pos')

        draw('initial', [0.0, 0.0, -115.63])

        frc = np.zeros((3, 3))
        frc[:, 1] = 100000
        h2.set_distributed_section_force_and_moment(ds, sec_frc=frc, sec_mom=frc * 0)
        h2.solver_static_run(reset_structure=True)
        draw('set frc + static solver', [0.0, 1.8293, -115.6123])
        c2_def = np.concatenate([pos, pos[:, :1]], 1)
        c2_def[:, 0] = np.r_[np.arange(0, 60, 10), np.arange(50, 0, -10)]
        tower_id = h2.get_mainbody_name_dict()["tower"]
        h2.set_c2_def(tower_id, c2_def)
        draw('set_c2_def', [10.0, 0.1184, -115.6296])
        h2.solver_static_run(reset_structure=True)
        draw('static solver', [10.2695, 2.8081, -115.5122])
        h2.set_distributed_section_force_and_moment(ds, sec_frc=-frc, sec_mom=frc * 0)
        h2.solver_static_run(reset_structure=True)
        draw('set -frc + static solver', [10.2695, -2.8081, -115.5122])
        if 0:
            plt.legend()
            plt.show()
        else:
            plt.close('all')


def test_set_distributed_section_force_and_moment_coo():
    with H2Lib() as h2:
        model_path = f"{tfp}DTU_10_MW/"
        htc = HTCFile(model_path + "htc/DTU_10MW_RWT_only_tower.htc")
        htc.new_htc_structure.orientation.base.body_eulerang = 0, 0, 90
        htc.save(model_path + "htc/DTU_10MW_RWT_only_tower_rot90.htc")
        h2.init(htc_path=htc.filename, model_path=model_path)
        ds = h2.add_distributed_sections(mainbody_name='tower', section_relative_position=[0, .5, 1])
        with pytest.raises(AssertionError, match='Call initialize_distributed_sections before get_distributed_section_force_and_moment'):
            h2.get_distributed_section_force_and_moment(ds)

        h2.initialize_distributed_sections()

        ax = plt.figure().add_subplot(projection='3d')

        def draw(label, ref):
            h2.solver_static_run()
            pos = h2.get_mainbody_nodes_state(mainbody_nr=1, state='pos')
            # print(label, np.round(pos[-1], 4).tolist())
            ax.plot(*pos.T, marker='.', label=label)
            npt.assert_array_almost_equal(pos[-1], ref, 4)

        draw('init', [0.0, 0.0, -115.6281])
        frc = np.zeros((3, 3))
        frc[:, 1] = 2e6
        h2.set_distributed_section_force_and_moment(ds, sec_frc=frc, sec_mom=frc * 0)
        draw('frc_y_global', [0.0, 33.8576, -110.0939])

        h2.set_distributed_section_force_and_moment(ds, sec_frc=frc, sec_mom=frc * 0, mainbody_coo_nr=1)
        draw('frc_y_tower', [-33.8576, -0.0, -110.0939])

        if 0:
            ax.axis('equal')
            ax.set_zlim([0, -120])
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.plot([0, 0], [0, 10], label='global y')
            ax.plot([0, -10], [0, 0], label='tower y')
            ax.legend()
            plt.show()
        else:
            plt.close('all')


def test_set_frc_blade():
    with H2Lib(suppress_output=0) as h2:
        htc = DTU10MWSimple(rotor_speed=.6, pitch=0, nbodies=1)
        htc.set_name('DTU_10MW_RWT_fixed_rotspeed')
        htc.aero.aerocalc_method = 0
        htc.save()
        h2.init(htc_path=htc.filename, model_path=htc.modelpath)

        ds_lst = [h2.get_distributed_sections(LinkType.BLADE, link_id=i) for i in [1, 2, 3]]
        h2.solver_static_run()
        plot = Plot(h2, ds_lst)
        plot('initial', [-1])
        ini_tip_pos = [h2.get_distributed_section_position_orientation(ds, mainbody_coo_nr=0)[0][-1] for ds in ds_lst]
        ini_tip3_tsg = h2.get_distributed_section_position_orientation(ds_lst[2], mainbody_coo_nr=9)[1][-1]
        zeros = np.zeros((50, 3))
        h2.set_distributed_section_force_and_moment(ds=ds_lst[0], sec_frc=zeros + [10000, 0, 0], sec_mom=zeros)
        h2.set_distributed_section_force_and_moment(ds=ds_lst[1], sec_frc=zeros + [0, 10000, 0], sec_mom=zeros)
        h2.set_distributed_section_force_and_moment(ds=ds_lst[2], sec_frc=zeros, sec_mom=zeros + [0, 0, 100000])
        h2.solver_static_run()

        plot('deflected', [-1])
        def_tip_pos = [h2.get_distributed_section_position_orientation(ds, mainbody_coo_nr=0)[0][-1] for ds in ds_lst]
        def_tip3_tsg = h2.get_distributed_section_position_orientation(ds_lst[2], mainbody_coo_nr=9)[1][-1]
        npt.assert_array_almost_equal(np.array(def_tip_pos) - ini_tip_pos,
                                      [[7.545511, -0.270957, 0.189638],  # mainly x
                                       [0.942178, 11.676871, 2.980586],  # mainly y
                                       [0.596675, -6.677523, -2.850951]],  # complex due to bend-twist coupling
                                      6)

        npt.assert_array_almost_equal(R.from_matrix(ini_tip3_tsg @ def_tip3_tsg).as_euler('xyz', 1),
                                      [30.762956, 0.310381, 44.774262], 6)  # rotation around z (but also x due to bend-twist coupling
        plot.show(0)


@pytest.mark.parametrize('coo_nr', [-1, 0, 1])
def test_get_set_frc_blade(coo_nr):
    '''
    1 Run static solver with aerodynamic and extract position, frc and mom of distributed sections
    2 New simulation, set frc and mom and run static solver without aerocalc
    3 compare position of distributed sections
    '''
    with H2Lib(suppress_output=0) as h2:
        htc = DTU10MWSimple(rotor_speed=.6, pitch=0, nbodies=1)
        htc.set_name('DTU_10MW_RWT_fixed_rotspeed')
        htc.simulation.convergence_limits.delete()
        htc.wind.wsp = 10
        htc.aero.tiploss_method = 0  # tiploss makes the static solver unstable
        htc.save()
        h2.init(htc_path=htc.filename, model_path=htc.modelpath)

        aero_ds_lst = [h2.get_distributed_sections(LinkType.BLADE, link_id=i) for i in [1, 2, 3]]

        mb_dict = h2.get_mainbody_name_dict()
        p = h2.get_distributed_section_position_orientation(aero_ds_lst[0], mb_dict['blade1'])[0]
        r = np.r_[0, np.cumsum(np.sqrt((np.diff(p, 1, 0)**2).sum(1)))]  # curve-length radius
        rR = r / r[-1]
        for ds in aero_ds_lst:
            h2.add_distributed_sections(ds.name, rR)
        h2.initialize_distributed_sections()

        body_ds_lst = [h2.get_distributed_sections(link_type=LinkType.BODY, link_id=i) for i in [1, 2, 3]]

        plot = Plot(h2, aero_ds_lst)
        h2.solver_static_run()
        plot('aerosections after static solver')
        # plot('bodysections after static solver', ds_lst=body_ds_lst)
        pos_coo = np.maximum(coo_nr, 0)
        ref_pos = [h2.get_distributed_section_position_orientation(ds, pos_coo)[0] for ds in aero_ds_lst]
        aero2body = [np.array(h2.get_distributed_section_position_orientation(aero_ds, pos_coo)[0]) -
                     h2.get_distributed_section_position_orientation(body_ds, pos_coo)[0]
                     for aero_ds, body_ds in zip(aero_ds_lst, body_ds_lst)]
        frc, mom = zip(*[h2.get_distributed_section_force_and_moment(ds, mainbody_coo_nr=coo_nr)
                       for ds in aero_ds_lst])
        if coo_nr == 0:
            aero_frc = h2.get_aerosections_forces()
            aero_mom = h2.get_aerosections_moments()
            aero_pos = h2.get_aerosections_position()
            npt.assert_array_equal(aero_frc, frc)
            npt.assert_array_almost_equal(aero_mom, mom)

            npt.assert_array_equal(ref_pos, aero_pos)

    with H2Lib(suppress_output=0) as h2:
        htc = DTU10MWSimple(rotor_speed=.6, pitch=0, nbodies=1)
        htc.simulation.convergence_limits.delete()
        htc.set_name('DTU_10MW_RWT_fixed_rotspeed')
        htc.aero.aerocalc_method = 0
        htc.save()
        h2.init(htc_path=htc.filename, model_path=htc.modelpath)

        aero_ds_lst = [h2.get_distributed_sections(LinkType.BLADE, link_id=i) for i in [1, 2, 3]]

        # set_distributed_section_force_and_moment maps the moment from section moments to moments around
        # elastic axis. This mapping depends on the deflection, so we need to run a couple of times to
        # get the right deflection and thereby the right mapping
        for _ in range(5):
            for sec_frc, sec_mom, ds in zip(frc, mom, aero_ds_lst):
                h2.set_distributed_section_force_and_moment(ds, sec_frc, sec_mom, mainbody_coo_nr=coo_nr)
            h2.solver_static_run()

        pos = [h2.get_distributed_section_position_orientation(ds, np.maximum(coo_nr, 0))[0] for ds in aero_ds_lst]
        plot = Plot(h2, aero_ds_lst, ax=plot.ax)
        plot('set frc')
        plot.show(0)
        npt.assert_array_almost_equal(ref_pos, pos)

    if coo_nr >= 0:
        # for global and blade1 coordinates:
        # apply forces and moments (mapped to c2df) to distributed sections (at c2def)
        # and compare position of aerodynamic sections
        with H2Lib(suppress_output=0) as h2:
            htc = DTU10MWSimple(rotor_speed=.6, pitch=0, nbodies=1)
            htc.simulation.convergence_limits.delete()
            htc.set_name('DTU_10MW_RWT_fixed_rotspeed')
            htc.aero.aerocalc_method = 0
            htc.save()
            h2.init(htc_path=htc.filename, model_path=htc.modelpath)

            aero_ds_lst = [h2.get_distributed_sections(LinkType.BLADE, link_id=i) for i in [1, 2, 3]]

            for ds in aero_ds_lst:
                h2.add_distributed_sections(ds.name, rR)
            h2.initialize_distributed_sections()

            body_ds_lst = [h2.get_distributed_sections(link_type=LinkType.BODY, link_id=i) for i in [1, 2, 3]]

            # set_distributed_section_force_and_moment maps the moment from section moments to moments around
            # elastic axis. This mapping depends on the deflection, so we need to run a couple of times to
            # get the right deflection and thereby the right mapping
            for _ in range(5):
                for sec_frc, sec_mom, ds, a2b in zip(frc, mom, body_ds_lst, aero2body):
                    body_mom = sec_mom + np.cross(sec_frc, -a2b)
                    h2.set_distributed_section_force_and_moment(ds, sec_frc, body_mom, mainbody_coo_nr=coo_nr)
                h2.solver_static_run()
            pos = [h2.get_distributed_section_position_orientation(ds, np.maximum(coo_nr, 0))[0] for ds in aero_ds_lst]
            plot = Plot(h2, aero_ds_lst, ax=plot.ax)
            plot('set frc')
            plot.show(0)
            # not sure why the accuracy is much worse. Maybe the distributed
            npt.assert_array_almost_equal(ref_pos, pos, 2)
