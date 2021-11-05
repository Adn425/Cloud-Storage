import dropbox

class TransferData:

    def_init_(self, access_token):
        self.access_token = access_token

    def upload.file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            f = open(file_from, 'rb')

            dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.A7se41tmbkLwxOxRB_LFMmVDIwGqLxPsyHGIqZvuA_FdtN3JojDGQiTJkQGtIBFh11OPV25JTRThHNgwhtUxPV-AfCtdQv0QlbHOay1aKOG9E4m-CwookeZP9JGZ0UGuxVoeN2M"
    TransferData = TransferData(access_token)

    file_from = input("C:\Users\Taha\Desktop\Adn\Module3\Cloud Storage\TestFolder")
    file_to = input("C:\Users\Taha\Desktop\Adn\Module3\OpenFiles")
    TransferData.upload_file(file_from, file_to)
    print("Just a sample")
main()

