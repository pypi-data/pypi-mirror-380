from __future__ import annotations
from vendy_bc import core
from vendy_bc.core import io
from vendy_bc.cli import main, color, dialog_creator, server_cli


class SaveManagement:
    def __init__(self):
        pass

    @staticmethod
    def save_save(save_file: core.SaveFile, check_strict: bool = True):
        """Save the save file without a dialog.

        Args:
            save_file (core.SaveFile): The save file to save.
        """
        SaveManagement.upload_items_checker(save_file, check_strict)

        if save_file.save_path is None:
            save_file.save_path = main.Main.save_save_dialog(save_file)

        if save_file.save_path is None:
            return

        save_file.to_file(save_file.save_path)

        color.ColoredText.localize("save_success", path=save_file.save_path)

    @staticmethod
    def save_save_dialog(save_file: core.SaveFile):
        """Save the save file with a dialog.

        Args:
            save_file (core.SaveFile): The save file to save.
        """
        SaveManagement.upload_items_checker(save_file)
        save_file.save_path = main.Main.save_save_dialog(save_file)
        if save_file.save_path is None:
            return

        save_file.to_file(save_file.save_path)

        color.ColoredText.localize("save_success", path=save_file.save_path)

    @staticmethod
    def save_save_documents(save_file: core.SaveFile):
        """Save the save file to the documents folder.

        Args:
            save_file (core.SaveFile): The save file to save.
        """
        import datetime
        SaveManagement.upload_items_checker(save_file)
        now = datetime.datetime.now()
        filename = now.strftime("SAVE_DATA_%Y%m%d_%H%M%S")
        save_path = core.SaveFile.get_saves_path().add(filename)
        save_file.save_path = save_path
        save_file.to_file(save_file.save_path)
        color.ColoredText("save_success", path=save_file.save_path)

    @staticmethod
    def save_upload(save_file: core.SaveFile):
        """Save the save file and upload it to the server.

        Args:
            save_file (core.SaveFile): The save file to save.
        """
        if core.core_data.config.get_bool(core.ConfigKey.STRICT_BAN_PREVENTION):
            color.ColoredText.localize("strict_ban_prevention_enabled")
            SaveManagement.create_new_account(save_file)

        result = core.ServerHandler(save_file).get_codes()
        if result is not None:
            SaveManagement.save_save(save_file, check_strict=False)
            transfer_code, confirmation_code = result
            color.ColoredText.localize(
                "upload_result",
                transfer_code=transfer_code,
                confirmation_code=confirmation_code,
            )
        else:
            color.ColoredText.localize("upload_fail")
            SaveManagement.save_save(save_file, check_strict=False)

    @staticmethod
    def unban_account(save_file: core.SaveFile):
        """Unban the account.

        Args:
            save_file (core.SaveFile): The save file to unban.
        """
        server_handler = core.ServerHandler(save_file)
        success = server_handler.create_new_account()
        if success:
            color.ColoredText.localize("unban_success")
        else:
            color.ColoredText.localize("unban_fail")

    @staticmethod
    def create_new_account(save_file: core.SaveFile):
        """Create a new account.

        Args:
            save_file (core.SaveFile): The save file to create a new account.
        """
        server_handler = core.ServerHandler(save_file)
        success = server_handler.create_new_account()
        if success:
            color.ColoredText.localize("create_new_account_success")
        else:
            color.ColoredText.localize("create_new_account_fail")

    @staticmethod
    def adb_push(save_file: core.SaveFile) -> core.AdbHandler | None:
        """Push the save file to the device.

        Args:
            save_file (core.SaveFile): The save file to push.

        Returns:
            core.AdbHandler: The AdbHandler instance.
        """
        SaveManagement.save_save(save_file)
        try:
            adb_handler = core.AdbHandler()
        except core.AdbNotInstalled:
            core.AdbHandler.display_no_adb_error()
            return None
        success = adb_handler.select_device()
        if not success:
            return adb_handler
        if save_file.used_storage and save_file.package_name is not None:
            adb_handler.set_package_name(save_file.package_name)
        else:
            packages = adb_handler.get_battlecats_packages()
            package_name = SaveManagement.select_package_name(packages)
            if package_name is None:
                color.ColoredText.localize("no_package_name_error")
                return adb_handler
            adb_handler.set_package_name(package_name)
        if save_file.save_path is None:
            return adb_handler
        result = adb_handler.load_battlecats_save(save_file.save_path)
        if result.success:
            color.ColoredText.localize("adb_push_success")
        else:
            color.ColoredText.localize("adb_push_fail", error=result.result)

        return adb_handler

    @staticmethod
    def adb_push_rerun(save_file: core.SaveFile):
        """Push the save file to the device and rerun the game.

        Args:
            save_file (core.SaveFile): The save file to push.
        """
        adb_handler = SaveManagement.adb_push(save_file)
        if not adb_handler:
            return
        if adb_handler.package_name is None:
            return
        result = adb_handler.rerun_game()
        if result.success:
            color.ColoredText.localize("adb_rerun_success")
        else:
            color.ColoredText.localize("adb_rerun_fail", error=result.result)

    @staticmethod
    def export_save(save_file: core.SaveFile):
        """Export the save file to a json file.

        Args:
            save_file (core.SaveFile): The save file to export.
        """
        data = save_file.to_dict()
        path = main.Main.save_json_dialog(data)
        if path is None:
            return
        data = core.JsonFile.from_object(data).to_data()
        data.to_file(path)
        color.ColoredText.localize("export_success", path=path)

    @staticmethod
    def init_save(save_file: core.SaveFile):
        """Initialize the save file to a new save file.

        Args:
            save_file (core.SaveFile): The save file to initialize.
        """
        confirm = dialog_creator.YesNoInput().get_input_once(
            "init_save_confirm"
        )
        if not confirm:
            return
        save_file.init_save(save_file.game_version)
        color.ColoredText.localize("init_save_success")

    @staticmethod
    def upload_items(save_file: core.SaveFile, check_strict: bool = True):
        """Upload the items to the server.

        Args:
            save_file (core.SaveFile): The save file to upload.
        """
        if (
            core.core_data.config.get_bool(core.ConfigKey.STRICT_BAN_PREVENTION)
            and check_strict
        ):
            color.ColoredText.localize("strict_ban_prevention_enabled")
            SaveManagement.create_new_account(save_file)

        server_handler = core.ServerHandler(save_file)
        success = server_handler.upload_meta_data()
        if success:
            color.ColoredText.localize("upload_items_success")
        else:
            color.ColoredText.localize("upload_items_fail")

    @staticmethod
    def upload_items_checker(
        save_file: core.SaveFile, check_strict: bool = True
    ):
        managed_items = core.BackupMetaData(save_file).get_managed_items()
        if not managed_items:
            return
        should_upload = dialog_creator.YesNoInput().get_input_once(
            "upload_items_checker_confirm"
        )
        if not should_upload:
            return
        SaveManagement.upload_items(save_file, check_strict)

    @staticmethod
    def select_save(starting_options: bool = False) -> core.SaveFile | None:
        """Select a new save file.

        Args:
            starting_options (bool, optional): Whether to add the starting specific options. Defaults to False.


        Returns:
            core.SaveFile | None: The save file.
        """
        options = [
            "download_save",
            "select_save_file",
            "load_from_documents",
            "adb_pull_save",
            "load_save_data_json",
            "create_new_save",
        ]
        if starting_options:
            options.append("edit_config")
            options.append("update_external")
            options.append("exit")

        root_handler = io.root_handler.RootHandler()

        if root_handler.is_android():
            options[2] = "root_storage_pull_save"

        choice = dialog_creator.ChoiceInput(
            options, options, [], {}, "save_load_option", True
        ).get_input_locale_while()
        if choice is None:
            return None
        choice = choice[0] - 1

        save_path = None
        cc: core.CountryCode | None = None
        used_storage = False
        package_name = None

        if choice == 0:
            data = server_cli.ServerCLI().download_save()
            if data is not None:
                save_path, cc = data
            else:
                save_path = None
        elif choice == 1:
            save_path = main.Main.load_save_file()
        elif choice == 2:
            save_path = core.SaveFile.get_saves_path().add("SAVE_DATA")
            if not save_path.exists():
                color.ColoredText.localize("save_file_not_found")
                return None
        elif choice == 3:
            handler = root_handler
            if not root_handler.is_android():
                try:
                    handler = core.AdbHandler()
                except core.AdbNotInstalled:
                    core.AdbHandler.display_no_adb_error()
                    return None
                if not handler.select_device():
                    return None

            package_names = handler.get_battlecats_packages()

            package_name = SaveManagement.select_package_name(package_names)
            if package_name is None:
                color.ColoredText.localize("no_package_name_error")
                return None
            handler.set_package_name(package_name)
            if root_handler.is_android():
                key = "storage_pulling"
            else:
                key = "adb_pulling"
            color.ColoredText.localize(key, package_name=package_name)
            save_path, result = handler.save_locally()
            if save_path is None:
                if root_handler.is_android():
                    color.ColoredText.localize(
                        "storage_pull_fail",
                        package_name=package_name,
                        error=result.result,
                    )
                else:
                    color.ColoredText.localize(
                        "adb_pull_fail",
                        package_name=package_name,
                        error=result.result,
                    )
            else:
                used_storage = True
        elif choice == 4:
            data = main.Main.load_save_data_json()
            if data is not None:
                save_path, cc = data
            else:
                save_path = None
        elif choice == 5:
            color.ColoredText.localize("create_new_save_warning")
            cc = core.CountryCode.select()
            if cc is None:
                return None
            try:
                gv = core.GameVersion.from_string(
                    color.ColoredInput().localize(
                        "game_version_dialog",
                    )
                )
            except ValueError:
                color.ColoredText.localize("invalid_game_version")
                return
            save = core.SaveFile(cc=cc, gv=gv, load=False)
            save_path = main.Main.save_save_dialog(save)
            if save_path is None:
                return None
            save.to_file(save_path)
            color.ColoredText.localize("create_new_save_success")

        elif choice == 6 and starting_options:
            core.core_data.config.edit_config()
        elif choice == 7 and starting_options:
            core.update_external_content()
        elif choice == 8 and starting_options:
            main.Main.exit_editor(check_temp=False)

        if save_path is None or not save_path.exists():
            return None

        color.ColoredText.localize("save_file_found", path=save_path)

        try:
            save_file = core.SaveFile(
                save_path.read(), cc, package_name=package_name
            )
        except core.CantDetectSaveCCError:
            color.ColoredText.localize("cant_detect_cc")
            cc = core.CountryCode.select()
            if cc is None:
                return None
            try:
                save_file = core.SaveFile(save_path.read(), cc)
            except Exception:
                tb = core.core_data.logger.get_traceback()
                color.ColoredText.localize("parse_save_error", error=tb)
                return None

        except Exception:
            tb = core.core_data.logger.get_traceback()
            color.ColoredText.localize("parse_save_error", error=tb)
            return None

        save_file.save_path = save_path
        save_file.save_path.copy_thread(save_file.get_default_path())
        save_file.used_storage = used_storage

        return save_file

    @staticmethod
    def select_package_name(package_names: list[str]) -> str | None:
        choice = dialog_creator.ChoiceInput.from_reduced(
            package_names,
            dialog="select_package_name",
            single_choice=True,
            localize_options=False,
        ).single_choice()
        if choice is None:
            return None
        return package_names[choice - 1]

    @staticmethod
    def load_save(save_file: core.SaveFile):
        """Load a new save file.

        Args:
            save_file (core.SaveFile): The current save file.
        """
        SaveManagement.upload_items_checker(save_file)
        new_save_file = SaveManagement.select_save()
        if new_save_file is None:
            return
        save_file.load_save_file(new_save_file)
        color.ColoredText.localize("load_save_success")

    @staticmethod
    def convert_save_cc(save_file: core.SaveFile):
        color.ColoredText.localize("cc_warning", current=save_file.cc)
        ccs_to_select = core.CountryCode.get_all()
        cc = core.CountryCode.select_from_ccs(ccs_to_select)
        if cc is None:
            return
        save_file.set_cc(cc)
        core.ServerHandler(save_file).create_new_account()
        color.ColoredText.localize("country_code_set", cc=cc)

    @staticmethod
    def convert_save_gv(save_file: core.SaveFile):
        color.ColoredText.localize(
            "gv_warning", current=save_file.game_version.to_string()
        )
        try:
            gv = core.GameVersion.from_string(
                color.ColoredInput().localize("game_version_dialog")
            )
        except ValueError:
            color.ColoredText.localize("invalid_game_version")
            return
        save_file.set_gv(gv)
        color.ColoredText.localize("game_version_set", version=gv.to_string())
