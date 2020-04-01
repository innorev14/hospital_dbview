# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    '''
    dept :진료과
    '''
    dept = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'department'


class DeptAndKeyword(models.Model):
    '''
    dept_id : 진료과
    name : 키워드
    '''
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept', primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dept_and_keyword'
        unique_together = (('dept', 'name'),)


class DepthOneKeyword(models.Model):
    '''
    name : 키워드
    '''
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'depth_one_keyword'


class DepthOneRel(models.Model):
    '''
    keyword : 1차 키워드
    relkeyword : 연관키워드
    source : 출처
    '''
    keyword = models.CharField(primary_key=True, max_length=50)
    relkeyword = models.CharField(max_length=50)
    source = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'depth_one_rel'
        unique_together = (('keyword', 'relkeyword'),)


class DepthThreeKeyword(models.Model):
    '''
    name : 연관키워드에 대한 연관 키워드
    '''
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'depth_three_keyword'


class DepthThreeRel(models.Model):
    '''
    keyword :  키워드
    relkeyword : 연관키워드
    '''
    keyword = models.CharField(primary_key=True, max_length=50)
    relkeyword = models.CharField(max_length=50)
    source = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'depth_three_rel'
        unique_together = (('keyword', 'relkeyword'),)


class DepthTwoKeyword(models.Model):
    '''
    name : Deth2 키워드
    '''
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'depth_two_keyword'


class DepthTwoRel(models.Model):
    '''
    keyword : #키워드
    relkeyword : 연관키워드
    source : 출처
    '''
    keyword = models.CharField(primary_key=True, max_length=50)
    relkeyword = models.CharField(max_length=50)
    source = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'depth_two_rel'
        unique_together = (('keyword', 'relkeyword'),)


class ExcludeWord(models.Model):
    '''
    name : 제외키워드
    '''
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'exclude_word'


class GoogleKeyword(models.Model):
    '''
    name : 구글 키워드
    '''
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'google_keyword'


class GoogleRelkeyword(models.Model):
    '''
    keyword : 구글 키워드
    relkeyword : 구글 연관키워드
    '''
    keyword = models.ForeignKey(GoogleKeyword, models.DO_NOTHING,
                                db_column='keyword', related_name='google_keyword', primary_key=True)
    relkeyword = models.ForeignKey(GoogleKeyword, models.DO_NOTHING,
                                   db_column='relkeyword', related_name='google_relkeyword')

    class Meta:
        managed = False
        db_table = 'google_relkeyword'
        unique_together = (('keyword', 'relkeyword'),)


class InstaAcctInfo(models.Model):
    top_post_url = models.CharField(primary_key=True, max_length=255)
    crawling_date = models.DateField()
    postcontent = models.CharField(db_column='postContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    postcomments = models.CharField(db_column='postComments', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    imgsrc = models.CharField(db_column='imgSrc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    likes = models.CharField(max_length=50, blank=True, null=True)
    postuploaddate = models.CharField(db_column='postUploadDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instaid = models.CharField(db_column='instaId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profileimage = models.CharField(db_column='profileImage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    postscount = models.CharField(db_column='postsCount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    followercount = models.CharField(db_column='followerCount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    followingcount = models.CharField(db_column='followingCount', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insta_acct_info'


class InstaAcctRel(models.Model):
    hashtag = models.CharField(primary_key=True, max_length=50)
    top_post_url = models.CharField(max_length=255)
    crawling_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'insta_acct_rel'
        unique_together = (('hashtag', 'top_post_url', 'crawling_date'),)


class InstaHashtagInfo(models.Model):
    hashtag = models.CharField(primary_key=True, max_length=50)
    num_post = models.CharField(max_length=50, blank=True, null=True)
    rel_tag_list = models.CharField(max_length=255, blank=True, null=True)
    totalnum_rel_tag_post = models.CharField(max_length=50, blank=True, null=True)
    auto_tag_list = models.CharField(max_length=255, blank=True, null=True)
    totalnum_auto_tag_post = models.CharField(max_length=50, blank=True, null=True)
    crawling_date = models.DateField()
    top_post_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insta_hashtag_info'
        unique_together = (('hashtag', 'crawling_date'),)


class JamesKeywordNaverapi(models.Model):
    '''
    date_id : 조회일자
    keyword : 키워드
    relkeyword : 연관키워드
    pcclick : pc클릭수
    mobileclick : 모바일 클릭수
    pcadsclick : pc 광고클릭수
    mobileadsclick : 모바일 광고클릭수
    pcpercentage :
    mobilepercentage :
    avgdepth :
    compidx : 경쟁도
    '''
    date_id = models.IntegerField(primary_key=True)
    relkeyword = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    pcclick = models.IntegerField(db_column='pcClick', blank=True, null=True)  # Field name made lowercase.
    mobileclick = models.IntegerField(db_column='mobileClick', blank=True, null=True)  # Field name made lowercase.
    pcadsclick = models.FloatField(db_column='pcAdsClick', blank=True, null=True)  # Field name made lowercase.
    mobileadsclick = models.FloatField(db_column='mobileAdsClick', blank=True, null=True)  # Field name made lowercase.
    pcpercentage = models.FloatField(db_column='pcPercentage', blank=True, null=True)  # Field name made lowercase.
    mobilepercentage = models.FloatField(db_column='mobilePercentage', blank=True, null=True)  # Field name made lowercase.
    avgdepth = models.IntegerField(db_column='AvgDepth', blank=True, null=True)  # Field name made lowercase.
    compidx = models.CharField(db_column='compIdx', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'james_keyword_naverapi'
        unique_together = (('date_id', 'relkeyword', 'keyword'),)


class JamesMainKeywordRel(models.Model):
    '''
    date_id : 조회일
    main_keyword : 키워드
    rel_keyword : 연관키워드
    '''
    date_id = models.IntegerField(primary_key=True)
    main_keyword = models.CharField(max_length=50)
    relkeyword = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'james_main_keyword_rel'
        unique_together = (('date_id', 'main_keyword', 'relkeyword'),)


class Keyword(models.Model):
    '''
    name : 키워드
    '''
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'keyword'


class ViewCountDevice(models.Model):
    '''
    date_id : 조회일
    name : 키워드
    pc : pc조회수
    mobile : 모바일조회수
    '''
    date_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    pc = models.IntegerField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_count_device'
        unique_together = (('date_id', 'name'),)


class ViewCountDeviceD3(models.Model):
    date_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    pc = models.IntegerField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_count_device_d3'
        unique_together = (('date_id', 'name'),)


class ViewCountGenderAge(models.Model):
    date_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    age0_12 = models.IntegerField(blank=True, null=True)
    age13_19 = models.IntegerField(blank=True, null=True)
    age20_24 = models.IntegerField(blank=True, null=True)
    age25_29 = models.IntegerField(blank=True, null=True)
    age30_39 = models.IntegerField(blank=True, null=True)
    age40_49 = models.IntegerField(blank=True, null=True)
    age50_field = models.IntegerField(db_column='age50_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'view_count_gender_age'
        unique_together = (('date_id', 'name', 'gender'),)


class ViewCountGenderAgeD3(models.Model):
    date_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    age0_12 = models.IntegerField(blank=True, null=True)
    age13_19 = models.IntegerField(blank=True, null=True)
    age20_24 = models.IntegerField(blank=True, null=True)
    age25_29 = models.IntegerField(blank=True, null=True)
    age30_39 = models.IntegerField(blank=True, null=True)
    age40_49 = models.IntegerField(blank=True, null=True)
    age50_field = models.IntegerField(db_column='age50_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'view_count_gender_age_d3'
        unique_together = (('date_id', 'name', 'gender'),)