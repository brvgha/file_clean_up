# Run actual script 
from src.file_clean_up import FileCleanUp
from src.utils import utils as u

root = '/posit/corpfs02/D_INFMEA'

output_path = '/posit/home/bfitzpat'


if __name__ == "__main__":
    try:
        u.setup()
        clean_up = FileCleanUp(root=root)
        clean_up.get_all_files()
        clean_up.get_file_info()

        print(clean_up.get_total_size_of_root())

        clean_up.write_to_csv(output_path=output_path)
        clean_up.write_fails(output_path=output_path)
    except OSError:
        print("❗❗❗ Drive is currently unavailable ❗❗❗")
    except KeyboardInterrupt:
        print("User has cancelled the process.")