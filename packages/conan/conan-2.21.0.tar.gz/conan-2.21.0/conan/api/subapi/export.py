from conan.api.output import ConanOutput
from conan.internal.cache.cache import PkgCache
from conan.internal.conan_app import ConanApp
from conan.internal.api.export import cmd_export
from conan.internal.methods import run_package_method
from conan.internal.graph.graph import BINARY_BUILD, RECIPE_INCACHE
from conan.api.model import PkgReference
from conan.internal.util.files import mkdir


class ExportAPI:

    def __init__(self, conan_api, helpers):
        self._conan_api = conan_api
        self._helpers = helpers

    def export(self, path, name, version, user, channel, lockfile=None, remotes=None):
        ConanOutput().title("Exporting recipe to the cache")
        app = ConanApp(self._conan_api)
        hook_manager = self._helpers.hook_manager
        return cmd_export(app, hook_manager, self._helpers.global_conf, path, name, version,
                          user, channel, graph_lock=lockfile, remotes=remotes)

    def export_pkg(self, deps_graph, source_folder, output_folder):
        cache = PkgCache(self._conan_api.cache_folder, self._helpers.global_conf)
        hook_manager = self._helpers.hook_manager

        # The graph has to be loaded with build_mode=[ref.name], so that node is not tried
        # to be downloaded from remotes
        # passing here the create_reference=ref argument is useful so the recipe is in "develop",
        # because the "package()" method is in develop=True already
        pkg_node = deps_graph.root
        ref = pkg_node.ref
        out = ConanOutput(scope=pkg_node.conanfile.display_name)
        out.info("Exporting binary from user folder to Conan cache")
        conanfile = pkg_node.conanfile

        package_id = pkg_node.package_id
        assert package_id is not None
        out.info("Packaging to %s" % package_id)
        pref = PkgReference(ref, package_id)
        pkg_layout = cache.create_build_pkg_layout(pref)

        conanfile.folders.set_base_folders(source_folder, output_folder)
        dest_package_folder = pkg_layout.package()
        conanfile.folders.set_base_package(dest_package_folder)
        mkdir(pkg_layout.metadata())
        conanfile.folders.set_base_pkg_metadata(pkg_layout.metadata())

        with pkg_layout.set_dirty_context_manager():
            prev = run_package_method(conanfile, package_id, hook_manager, ref)

        pref = PkgReference(pref.ref, pref.package_id, prev)
        pkg_layout.reference = pref
        cache.assign_prev(pkg_layout)
        pkg_node.prev = prev
        pkg_node.pref_timestamp = pref.timestamp  # assigned by assign_prev
        pkg_node.recipe = RECIPE_INCACHE
        pkg_node.binary = BINARY_BUILD
        # Make sure folder is updated
        final_folder = pkg_layout.package()
        conanfile.folders.set_base_package(final_folder)
        out.info(f"Package folder {final_folder}")
        out.success("Exported package binary")
