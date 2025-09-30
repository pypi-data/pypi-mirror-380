"""almastktestutils - utility module to be used for the maintenance of 
   test_stk_alma_pipeline_imaging.py
   
   extract_expdict: extract the fiducial metrics stored with tests in the old format
                    of test_stk_alma_pipeline_imaging.py

"""
import ast
import copy
import json
import os
import sys
import shutil


def extract_expdict(testlist=None, testsrcpath=None):
    """ Read old test_alma_stk_pipeline_imaging.py and extract
    exp dictionaries of the specific test and save to a json file
    """
    if testlist is None:
        testlist = []
    if not os.path.exists(testsrcpath):
        raise IOError(f"{testsrcpath} not found")

    if not testsrcpath.endswith('/'):
        testsrcpath += '/'
    oldstktestfile = testsrcpath + "test_stk_alma_pipeline_imaging.py"
    print("testcode =", oldstktestfile)
    if isinstance(testlist, list) and len(testlist) == 0:
        print(f"Scan all tests in {oldstktestfile}")
        sys.path.append(testsrcpath)
        from src.test_stk_alma_pipeline_imaging import Test_standard
        testlist.extend([testname for testname in dir(Test_standard) if testname.startswith('test_') is True])
    for testname in testlist:
        print(f"Processing {testname}.... ")

        outfile = testname + '_exp_dicts.json'
        # srcdir='/export/home/murasame/casa/casa6/'
        # testdir='casatests/stakeholder/'
        # abspath = srcdir+testdir

        with open(oldstktestfile) as f:
            readDict = False
            exp_im_stats_str = ""
            exp_im_stats_str_end = False
            exp_mask_stats_str = ""
            exp_mask_stats_str_end = False
            exp_pb_stats_str = ""
            exp_pb_stats_str_end = False
            exp_psf_stats_str = ""
            exp_psf_stats_str_end = False
            exp_model_stats_str = ""
            exp_model_stats_str_end = False
            exp_resid_stats_str = ""
            exp_resid_stats_str_end = False
            exp_sumwt_stats_str = ""
            exp_sumwt_stats_str_end = False
            exp_wt_stats_str = ""
            exp_wt_stats_str_end = False
            exp_bmin_dict_str = ""
            exp_bmaj_dict_str = ""
            exp_pa_dict_str = ""
            exp_im1_stats_str = ""
            exp_im1_stats_str_end = False
            exp_model1_stats_str = ""
            exp_model1_stats_str_end = False
            exp_resid1_stats_str = ""
            exp_resid1_stats_str_end = False
            exp_sumwt1_stats_str = ""
            exp_sumwt1_stats_str_end = False

            for ln in f:
                # skip the comment lines
                if ln.lstrip().startswith("#"):
                    pass
                else:
                    if "def " + testname + "(" in ln:
                        print(f"test {testname} found!")
                        readDict = True
                    elif 'def test_' in ln and readDict:
                        print(f"Finish reading {testname}")
                        break

                    # read each exp_ dictionary here (stop reading when detect "}"
                    if readDict:
                        if not exp_im_stats_str and "exp_im_stats = {" in ln:
                            exp_im_stats_str = ln.lstrip("exp_im_stats = ").rstrip("\n")
                        elif exp_im_stats_str and not exp_im_stats_str_end:
                            exp_im_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '').lstrip()
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_im_stats_str_end = True
                                print("Stop reading exp_im_stats")
                        elif not exp_mask_stats_str and "exp_mask_stats = {" in ln:
                            exp_mask_stats_str = ln.lstrip("exp_mask_stats = ").rstrip("\n")
                        elif exp_mask_stats_str and not exp_mask_stats_str_end:
                            exp_mask_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_mask_stats_str_end = True
                                print("Stop reading exp_mask_stats")
                        elif not exp_pb_stats_str and "exp_pb_stats = {" in ln:
                            exp_pb_stats_str = ln.lstrip("exp_pb_stats = ").rstrip("\n")
                        elif exp_pb_stats_str and not exp_pb_stats_str_end:
                            exp_pb_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_pb_stats_str_end = True
                                print("Stop reading exp_pb_stats")
                        elif not exp_psf_stats_str and "exp_psf_stats = {" in ln:
                            exp_psf_stats_str = ln.lstrip("exp_psf_stats = ").rstrip("\n")
                        elif exp_psf_stats_str and not exp_psf_stats_str_end:
                            exp_psf_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_psf_stats_str_end = True
                                print("Stop reading exp_psf_stats")
                        elif not exp_model_stats_str and "exp_model_stats = {" in ln:
                            exp_model_stats_str = ln.lstrip("exp_model_stats = ").rstrip("\n")
                        elif exp_model_stats_str and not exp_model_stats_str_end:
                            exp_model_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_model_stats_str_end = True
                                print("Stop reading exp_model_stats")
                        elif not exp_resid_stats_str and "exp_resid_stats = {" in ln:
                            exp_resid_stats_str = ln.lstrip("exp_resid_stats = ").rstrip("\n")
                        elif exp_resid_stats_str and not exp_resid_stats_str_end:
                            exp_resid_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_resid_stats_str_end = True
                                print("Stop reading exp_resid_stats")
                        elif not exp_sumwt_stats_str and "exp_sumwt_stats = {" in ln:
                            exp_sumwt_stats_str = ln.lstrip("exp_sumwt_stats = ").rstrip("\n")
                        elif exp_sumwt_stats_str and not exp_sumwt_stats_str_end:
                            exp_sumwt_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_sumwt_stats_str_end = True
                                print("Stop reading exp_sumwt_stats")
                        elif not exp_wt_stats_str and "exp_wt_stats = {" in ln:
                            exp_wt_stats_str = ln.lstrip("exp_wt_stats = ").rstrip("\n")
                        elif exp_wt_stats_str and not exp_wt_stats_str_end:
                            exp_wt_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_wt_stats_str_end = True
                                print("Stop reading exp_wt_stats")
                        elif not exp_bmin_dict_str and "exp_bmin_dict = {" in ln:
                            exp_bmin_dict_str = ln.lstrip("exp_bmin_dict = ").rstrip("\n")
                            # elif len(exp_bmin_dict_str) and not exp_bmin_dict_str_end:
                            #    exp_bmin_dict_str+=ln.rstrip("\n").rstrip(" ").replace("\\",'')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                print("Stop reading exp_bmin_dict")
                        elif not exp_bmaj_dict_str and "exp_bmaj_dict = {" in ln:
                            exp_bmaj_dict_str = ln.lstrip("exp_bmaj_dict = ").rstrip("\n")
                            # elif len(exp_bmaj_dict_str) and not exp_bmaj_dict_str_end:
                            #    exp_bmaj_dict_str+=ln.rstrip("\n").rstrip(" ").replace("\\",'')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                print("Stop reading exp_bmaj_dict")
                        elif not exp_pa_dict_str and "exp_pa_dict = {" in ln:
                            exp_pa_dict_str = ln.lstrip("exp_pa_dict = ").rstrip("\n")
                            # elif len(exp_pa_dict_str) and not exp_pa_dict_str_end:
                            #    exp_pa_dict_str+=ln.rstrip("\n").rstrip(" ").replace("\\",'')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                print("Stop reading exp_pa_dict")
                        elif not exp_im1_stats_str and "exp_im1_stats = {" in ln:
                            exp_im1_stats_str = ln.lstrip("exp_im1_stats = ").rstrip("\n")
                        elif exp_im1_stats_str and not exp_im1_stats_str_end:
                            exp_im1_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_im1_stats_str_end = True
                                print("Stop reading exp_im1_stats")
                        elif not exp_model1_stats_str and "exp_model1_stats = {" in ln:
                            exp_model1_stats_str = ln.lstrip("exp_model1_stats = ").rstrip("\n")
                        elif exp_model1_stats_str and not exp_model1_stats_str_end:
                            exp_model1_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_model1_stats_str_end = True
                                print("Stop reading exp_model1_stats")
                        elif not exp_resid1_stats_str and "exp_resid1_stats = {" in ln:
                            exp_resid1_stats_str = ln.lstrip("exp_resid1_stats = ").rstrip("\n")
                        elif exp_resid1_stats_str and not exp_resid1_stats_str_end:
                            exp_resid1_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_resid1_stats_str_end = True
                                print("Stop reading exp_resid1_stats")
                        elif not exp_sumwt1_stats_str and "exp_sumwt1_stats = {" in ln:
                            exp_sumwt1_stats_str = ln.lstrip("exp_sumwt1_stats = ").rstrip("\n")
                        elif exp_sumwt1_stats_str and not exp_sumwt1_stats_str_end:
                            exp_sumwt1_stats_str += ln.rstrip("\n").rstrip(" ").replace("\\", '')
                            if ln.rstrip("\n").rstrip().endswith("}"):
                                exp_sumwt1_stats_str_end = True
                                print("Stop reading exp_sumwt1_stats")

            # if exp_im_stats_str_end and exp_mask_stats_str_end and exp_pb_stats_str_end:
            #    print("finish reading the test")
            #    readDict=False
            #    break

        outdict = {'exp_im_stats': ast.literal_eval(exp_im_stats_str),
                   'exp_mask_stats': ast.literal_eval(exp_mask_stats_str),
                   'exp_pb_stats': ast.literal_eval(exp_pb_stats_str),
                   'exp_psf_stats': ast.literal_eval(exp_psf_stats_str),
                   'exp_model_stats': ast.literal_eval(exp_model_stats_str),
                   'exp_resid_stats': ast.literal_eval(exp_resid_stats_str),
                   'exp_sumwt_stats': ast.literal_eval(exp_sumwt_stats_str)}
        if 'mosaic' in testname:
            outdict['exp_wt_stats'] = ast.literal_eval(exp_wt_stats_str)
        if 'cube' in testname and not ('eph' in testname):
            outdict['exp_bmin_dict'] = ast.literal_eval(exp_bmin_dict_str)
            outdict['exp_bmaj_dict'] = ast.literal_eval(exp_bmaj_dict_str)
            outdict['exp_pa_dict'] = ast.literal_eval(exp_pa_dict_str)
        if 'mtmfs' in testname:
            outdict['exp_im1_stats'] = ast.literal_eval(exp_im1_stats_str)
            outdict['exp_model1_stats'] = ast.literal_eval(exp_model1_stats_str)
            outdict['exp_resid1_stats'] = ast.literal_eval(exp_resid1_stats_str)
            outdict['exp_sumwt1_stats'] = ast.literal_eval(exp_sumwt1_stats_str)

        outdictwithTestname = {testname: outdict}
        with open(outfile, 'w') as outf:
            json.dump(outdictwithTestname, outf, indent=4)
        print("Extracted the fudicial value dictionaries is saved in a file, ", outfile)


def extract_subexpdict(jsonfile, keylist, outjsonfile=''):
    """
    Extract subset of metric values from a json file contains current metric values 
    from a single testcase by specifying metric names and output a new json file contains
    only the specfied subset of the metrics.

    jsonfile: json file for a single testcase (saved by savematricdict=True in 
             test_stk_alma_pipeline_imaging,py)
    keylist: a dictionary contains main_metric_key('eg. im_stats_dict..') with a list of 
    metric names to be extracted
    returns a dictionary only contains the main stats category key
    and metric (key+its value(s))
    outjsonfile: output json file containing the extracted dictionary (with top level key
                 word = testcase name)
    """
    outdict = {}

    if outjsonfile == '':
        outjsonfile = jsonfile.rstrip('.json') + '_subDict.json'
    with open(jsonfile, 'r') as f:
        indict = json.load(f)
    topkeyfound = False
    # the top key should be test case name
    topkey = list(indict.keys())[0]
    if 'test' in topkey:
        topkeyfound=True
        outdict[topkey]={}
        for k in keylist:
            if k in indict[topkey]:
                outdict[topkey][k]={}
                for metrickey in keylist:
                    if metrickey in indict[topkey][k]:
                        outdict[topkey][k].update({metrickey:indict[topkey][k][metrickey]})
            else:
                print("f{k} not found in the input json")
    else:
        print('No testcase name in the top key. Cannot process the json file')
        return False

    if outdict:
        with open(outjsonfile, 'w') as outf:
            json.dump(outdict, outf)
            print(f"Saving the sub-dictionary to {outjsonfile}")
    return outdict

def create_expdict_jsonfile(inmetricsfile, templatemetrics, outmetricsfile):
    """
    create the fiducial metric dictionaries
    from the corresponding metric dictionaries of the current
    run saved as a json file and also returned as a dictionary
    """
    infiles = [inmetricsfile, templatemetrics]
    for f in infiles:
        if not os.path.exists(f):
            raise Exception(f"{f} is not found")
    outDict = {}
    with open(templatemetrics, 'r') as tmplf, open(inmetricsfile, 'r') as curf, open(outmetricsfile, 'w') as outf:
        tmplFidDict = json.load(tmplf)
        curDict = json.load(curf)
        testname = list(curDict.keys())[0]
        if 'test_' in testname:
            if testname in curDict:
                outDict[testname] = {}
                subOutDict = outDict[testname]
                for expkey in tmplFidDict[testname]:
                    print("Processing expkey=", expkey)
                    if expkey != 'comment' and expkey != 'comments':
                        curkey = expkey[4:]  # name of the dict in the current metrics
                        isbeaminfo = False
                        if not curkey.endswith("_dict"):
                            curkey += "_dict"
                        else:
                            isbeaminfo = True
                        print("Processing curkey=", curkey)
                        #print("isbeaminfo=", isbeaminfo)
                        if curkey in curDict[testname]:
                            subOutDict[expkey] = {}
                            if isbeaminfo:
                                subOutDict[expkey] = curDict[testname][curkey]
                            else:
                                # loop through each metric inside the particular exp_ dict
                                for metrickey in tmplFidDict[testname][expkey]:
                                    # check to see if the metric exist in the input (current) metric dict
                                    if metrickey in curDict[testname][curkey]:
                                        #print("expkey={}, metrickey={}, metricbool={}".format(expkey, metrickey,
                                        #                                                  tmplFidDict[testname][expkey][
                                        #                                                      metrickey][0]))
                                        subOutDict[expkey][metrickey] = [tmplFidDict[testname][expkey][metrickey][0],
                                                                     curDict[testname][curkey][metrickey]]
                                    else:  # metric does not exist in input cur metric dicts
                                        raise Exception(
                                            f"Missing the metric key={metrickey} in {inmetricsfile}. Check the input file.")
                        else:
                            if curkey == 'bmin_dict' or curkey == 'bmaj_dict' or curkey == 'pa_dict':
                                print(f"Missing key={curkey} in {inmetricsfile}. The input json is probably made from serial run")
                            else:
                                raise Exception(f"Missing key={curkey} in {inmetricsfile}. Check the input file.")

                json.dump(outDict, outf, indent=4)
            else:
                raise Exception(
                    f"{inmetricsfile} does not contain test name {testname} as a top level key. Please modify the input file.")
        else:
            raise Exception(
                f"{tmplFidDict} does not contain a test name in the top key. Please modify the input file.")


def create_combined_expdict_jsonfile(jsonlist, outjson, casaversion):
    """
    make a single json to be used in alma stakeholder tests
    """
    outdict = {'casa_version': casaversion}
    with open(outjson, 'w') as outf:
        for jsonfile in jsonlist:
            try:
                with open(jsonfile, 'r') as inf:
                    testdict = json.load(inf)
                    if isinstance(testdict, dict):
                        testname = list(testdict.keys())[0]
                        if 'test_' in testname:
                            # check the version info of the test results
                            if 'casa_version' in testdict[testname]:
                                casaversionused = testdict['casa_version']
                                if casaversionused != casaversion:
                                    print(f'casa_version for {casaversionused} is different from expected casaversion: {casaversion}')
                            else:
                                print("No casa_version info in the input dictionary. Skip the check.")
                            outdict[testname] = copy.deepcopy(testdict[testname])
            except RuntimeError:
                print("Errors in reading the input json file. Check the input")
        if outdict:
            json.dump(outdict, outf)
        else:
            print("Error occured. No outfile is wriiten.")


def read_expdict_jsonfile(jsonfilename=None):
    """read the json file containing the fiducial metrics parameter values for all tests"""
    try:
        with open(jsonfilename, 'r') as fexp:
            return json.load(fexp)
    except RuntimeError:
        print("Error occurred in reading the json file for fiducial values")


def read_testcase_expdicts(jsonfilename, testcasename, version):
    try:
        with open(jsonfilename, 'r') as fexp:
            alltestdicts = json.load(fexp)
            # check a CASA version that exp_dicts based on
            if version != '':
                if 'casa_version' in alltestdicts.keys():
                    if version != alltestdicts['casa_version']:
                        raise SystemError(f'Mismatch in the fiducial data file version. The testcase expects fiducial '
                                          'values based on the CASA {version} ')
            if testcasename in alltestdicts:
                return alltestdicts[testcasename]
            else:
                raise Exception(f"key {testcasename} is not found in {jsonfilename} exp_dicts")
    except RuntimeError:
        print("Error occurred in reading the json file for fiducial values")


def update_expdict_jsonfile(newexpdictlist, jsonfilename):
    """Convert current metrics parameter values stored in json per test to the exp_dict json.
       The output will be an updated json file named jsonfilename+"_update"

       newexpdictlist: a list of name of json files, which are produced by running
       save_to_dict() inside each stakeholder testcase or can be produced. The list can
       consist of only the testcases that need to be updated and the exp_dicts for other
       testcases not in the list won't be modified and copy to the new json as is.

       jsonfilename: current json file contains all the fiducial metrics values

    """
    tmplFidDict = read_expdict_jsonfile(jsonfilename)
    newjsonfile = jsonfilename.split(".json")[0] + "_update.json"
    outDict = copy.deepcopy(tmplFidDict)


    for inmetricsfile in newexpdictlist:  # read current values for each testscase
        with open(inmetricsfile, 'r') as curf:
            curDict = json.load(curf)
            testname = list(curDict.keys())[0]
            if 'test_' in testname:
                if testname in tmplFidDict:
                    outDict[testname] = {}
                    subOutDict = outDict[testname]
                    for expkey in tmplFidDict[testname]:
                        print("Processing expkey=", expkey)
                        if expkey != 'comment' and expkey != 'comments':
                            curkey = expkey[4:]  # name of the dict in the current metrics
                            if not curkey.endswith("_dict"):
                                curkey += "_dict"
                            else:
                                isbeaminfo = True
                            print("Processing curkey=", curkey)
                            if curkey in curDict[testname]:
                                subOutDict[expkey] = {}
                                if isbeaminfo:
                                    subOutDict[expkey] = curDict[testname][curkey]
                                else:
                                    # loop through each metric inside the particular exp_ dict
                                    for metrickey in tmplFidDict[testname][expkey]:
                                        # check to see if the metric exist in the input (current) metric dict
                                        if metrickey in curDict[testname][curkey]:
                                            #  print("expkey={}, metrickey={}, metricbool={}".format(expkey, metrickey,
                                            #                                                    tmplFidDict[testname][
                                            #                                                        expkey][
                                            #                                                        metrickey][0]))
                                            subOutDict[expkey][metrickey] = [
                                                tmplFidDict[testname][expkey][metrickey][0],
                                                curDict[testname][curkey][metrickey]]
                                        else:  # metric does not exist in input cur metric dicts
                                            raise Exception(f"Missing the metric key={metrickey} in {inmetricsfile}. Check the input file")
                            else:
                                if curkey == 'bmin_dict' or curkey == 'bmaj_dict' or curkey == 'pa_dict':
                                    print(f"Missing key={curkey} in {inmetricsfile}. The input json is probably made from serial run.")
                                else:
                                    raise Exception(
                                        f"Missing key={curkey} in {inmetricsfile}. Check the input file.")
                    # end for-loop
                    json.dump(outDict, outf)
                else:
                    raise Exception(f"{inmetricsfile} does not contain test name {testname} as a top level key." +
                                    "Please modify the input file.")
            else:
                raise Exception(f"{tmplFidDict} does not contain a test name in the top key." +
                                "Please modify the input file.")
    with open(newjsonfile, 'w') as outf:
        json.dump(outDict, outf, indent=4)


def update_expdict_subset(expjsonfile, newvaldictjson, jiranoforcomment=''):
    """
    Replace selected metric values in combined (for all ALMA stk testcases) expdicts json
    with new values. The updated json file will be named input base file name with "_update.json"
    and is saved in the current working directory.
    expjsonfile: current combined exp json file (i.e. test_stk_alma_pipeline_imaging_exp_dicts.json)
                 Note: a copy of the file will be made in the current working directory 
    newvaldictjson: metric values to be updated (need to put in the same nested dictionary 
                structure as the expjsonfile with only relevant keys
    jiranoforcomment (optional): releant JIRA ticket number to be inserted as 'comment' 
    under the sub-dictionary section of the relevant testcase. The updated matrics names
    are also added to the comment section.
    """
    allreplaced = False
    basename = os.path.basename(expjsonfile)
    expjsonname = basename.split('.json')[0]
    outjsonfile = expjsonname+'_update.json'
    shutil.copy(expjsonfile, outjsonfile)

    with open(outjsonfile, 'r') as f:
        outdict = json.load(f)
    with open(newvaldictjson, 'r') as newvf:
        valdict = json.load(newvf)
 
    testcases =  list(valdict.keys())
    for tc in testcases:
        comment = 'Updated'
        if jiranoforcomment != '':
            comment += ' for '+jiranoforcomment
        comment +=': ' 
        if tc in outdict: # testcase name
            for k in valdict[tc]:
                expk = 'exp_'+k.rstrip('_dict')
                if expk in outdict[tc]:
                    comment += ' '+expk + ' ['
                    for mtk in valdict[tc][k]:
                        if mtk in outdict[tc][expk]:
                            # exp metrics should in a list (e.g. [T/F/tol, val]
                            if isinstance(outdict[tc][expk][mtk], list):
                                # Only change val part not comparison type (True/False/tol)
                                outdict[tc][expk][mtk][1]=valdict[tc][k][mtk]
                                comment += mtk+','
                                allreplaced = True
                            else:
                                print("Expecting a list for the matric value ([T/F/tal, val]",format(mtk))
                                allreplaced = False
                        else:
                            print(f"{mtk} is not found in the combined json. Skip this.")
                            allreplaced = False 
                    comment = comment.rstrip(',') + ']'
                
                else:
                    print(f"{expk} is not found in the combined json. Skip this.")
                    #print("outdict[tc].keys()=", outdict[tc].keys())
                    allreplaced = False 
                    return False
            outdict[tc]['comment']=comment 
        else:
            print(f"The testcase {tc} not found in the combined json. Check the input.")
            return False 
   
    if allreplaced:
        print(f"Writing to the updated values in {outjsonfile}")
        with open(outjsonfile, 'w+') as outf:
            json.dump(outdict,outf)
        return True
    else:
        return False
                
def compare_expdictjson(newjson, oldjson):
    """
    compare the two exp dicts - used to check updating of exp_dicts json file
    is done properly...
    """
    with open(oldjson, 'r') as fold, open(newjson, 'r') as fnew:
        newdict = json.load(fnew)
        olddict = json.load(fold)

        if newdict == olddict:
            return "The two json files are identical"
        else:
            # level 0 (testcase level)
            newkey0list = list(newdict.keys())
            oldkey0list = list(olddict.keys())
            newonlykey0 = set(newkey0list).difference(oldkey0list)
            oldonlykey0 = set(oldkey0list).difference(newkey0list)
            commonkey0 = set(newkey0list).intersection(oldkey0list)
            finaldiffdict = {}
            for key0 in commonkey0:
                # do for each testcase, extract set of metrics  for each image type
                if isinstance(newdict[key0], dict) and isinstance(olddict[key0], dict):
                    newkey1list = list(newdict[key0].keys())
                    oldkey1list = list(olddict[key0].keys())
                    newonlykey1 = set(newkey1list).difference(oldkey1list)
                    oldonlykey1 = set(oldkey1list).difference(newkey1list)
                    commonkey1 = set(newkey1list).intersection(oldkey1list)
                    for key1 in commonkey1:
                        if key1!='comment':
                            newkey2list = list(newdict[key0][key1].keys())
                            oldkey2list = list(olddict[key0][key1].keys())
                            newonlykey2 = set(newkey2list).difference(oldkey2list)
                            oldonlykey2 = set(oldkey2list).difference(newkey2list)
                            commonkey2 = set(newkey2list).intersection(oldkey2list)
                            # Comparison of the values and test threshold type
                            diffkey2dict = {}
                            for key2 in commonkey2:  # a list containing [thres. type, []]
                                if isinstance(olddict[key0][key1][key2], list):
                                    if olddict[key0][key1][key2][1] != newdict[key0][key1][key2][1]:
                                        if key2 not in diffkey2dict:
                                            diffkey2dict[key2] = {}
                                        diffkey2dict[key2]['msg'] = 'diff in value(s)'
                                        diffkey2dict[key2]['json1'] = newdict[key0][key1][key2]
                                        diffkey2dict[key2]['json2'] = olddict[key0][key1][key2]
                                    if olddict[key0][key1][key2][0] != newdict[key0][key1][key2][0]:
                                        if 'msg' in diffkey2dict[key2]:
                                            diffkey2dict[key2]['msg'] += ' and threshold type'
                                        else:
                                            diffkey2dict[key2]['msg'] = 'diff in threshold type'
                                            diffkey2dict[key2]['json1'] = newdict[key0][key1][key2][0]
                                            diffkey2dict[key2]['json2'] = olddict[key0][key1][key2][0]
                                else:
                                    # non metric values (possibly comments or version info)
                                    if olddict[key0][key1][key2] != newdict[key0][key1][key2]:
                                        diffkey2dict[key2] = \
                                            'json1: {}, json2: {}'.format(newdict[key0][key1][key2],
                                                                          olddict[key0][key1][key2])

                            if diffkey2dict != dict():
                                if key0 not in finaldiffdict:
                                    finaldiffdict[key0] = {}
                                if key1 not in finaldiffdict:
                                    finaldiffdict[key0][key1] = {}
                                finaldiffdict[key0][key1] = copy.deepcopy(diffkey2dict)
                            if newonlykey2 != set():
                                finaldiffdict[key0][key1]['metric keys only in json1'] = newonlykey2
                            if oldonlykey2 != set():
                                finaldiffdict[key0][key1]['metric keys only in json2'] = oldonlykey2
                        if newonlykey1 != set():
                            finaldiffdict[key0]['metric dict only in json1'] = newonlykey1
                        if oldonlykey1 != set():
                            finaldiffdict[key0]['metric dict only in json2'] = oldonlykey1
                else:
                    if newdict[key0] != olddict[key0]:
                        finaldiffdict[key0] = 'diff info json1: {}, json2: {}'.format(newdict[key0], olddict[key0])
            if newonlykey0 != set():
                finaldiffdict['testcase(s)/other info only in json1'] = newonlykey0
            if oldonlykey0 != set():
                finaldiffdict['testcase(s)/other info  only in json2'] = oldonlykey0
        return finaldiffdict
